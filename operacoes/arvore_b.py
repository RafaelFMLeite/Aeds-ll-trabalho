import os
import logging
from entidades.evento import Evento

# Verifica se a pasta 'dados' existe e cria se necessário
os.makedirs('dados', exist_ok=True)

# Configuração do logger para salvar o log na pasta 'dados'
logging.basicConfig(
    filename='dados/arvore_b_eventos.log',  # Caminho do arquivo de log
    filemode='w',  # Sobrescrever o arquivo a cada execução
    format='%(message)s',
    level=logging.INFO
)

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # True se o nó for folha
        self.keys = []    # Armazena eventos (ordenados por ID)
        self.children = []  # Armazena ponteiros para os filhos

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Grau mínimo (define o intervalo para o número de chaves)

    def search(self, id_evento, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and id_evento > x.keys[i].id_evento:
            i += 1
        if i < len(x.keys) and id_evento == x.keys[i].id_evento:
            return x.keys[i]
        elif x.leaf:
            return None
        else:
            return self.search(id_evento, x.children[i])

    def insert(self, evento):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            s = BTreeNode()
            self.root = s
            s.children.append(root)  # A raiz antiga se torna o 0º filho da nova raiz
            self._split_child(s, 0)
            self._insert_non_full(s, evento)
        else:
            self._insert_non_full(root, evento)

    def _insert_non_full(self, x, evento):
        if x.leaf:
            i = len(x.keys) - 1
            x.keys.append(None)
            while i >= 0 and evento.id_evento < x.keys[i].id_evento:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = evento
        else:
            i = len(x.keys) - 1
            while i >= 0 and evento.id_evento < x.keys[i].id_evento:
                i -= 1
            i += 1

            if len(x.children) <= i:
                x.children.append(BTreeNode(leaf=True))  # Inicializar filho se não existir

            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if evento.id_evento > x.keys[i].id_evento:
                    i += 1

            self._insert_non_full(x.children[i], evento)

    def _split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t]

    def delete(self, id_evento):
        self._delete(self.root, id_evento)
        if len(self.root.keys) == 0:
            if not self.root.leaf:
                self.root = self.root.children[0]  # Se a raiz estiver vazia e tiver filhos, mova para o primeiro filho
            else:
                self.root = BTreeNode(True)  # Se não, crie uma nova raiz vazia

    def _delete(self, x, id_evento):
        t = self.t
        i = 0
        while i < len(x.keys) and id_evento > x.keys[i].id_evento:
            i += 1

        if i < len(x.keys) and id_evento == x.keys[i].id_evento:  # Se o evento está neste nó
            if x.leaf:
                x.keys.pop(i)  # Remova da folha
            else:
                self._delete_internal_node(x, id_evento, i)
        elif not x.leaf:
            if len(x.children[i].keys) < t:  # Se o filho tem menos que t chaves
                self._fill(x, i)
            self._delete(x.children[i], id_evento)
        else:
            return  # O evento não está na árvore

    def _delete_internal_node(self, x, id_evento, i):
        t = self.t
        if len(x.children[i].keys) >= t:  # Caso 1: Predecessor
            pred = self._get_predecessor(x, i)
            x.keys[i] = pred
            self._delete(x.children[i], pred.id_evento)
        elif len(x.children[i + 1].keys) >= t:  # Caso 2: Sucessor
            succ = self._get_successor(x, i)
            x.keys[i] = succ
            self._delete(x.children[i + 1], succ.id_evento)
        else:  # Caso 3: Combina os filhos
            self._merge(x, i)
            self._delete(x.children[i], id_evento)

    def _get_predecessor(self, x, i):
        current = x.children[i]
        while not current.leaf:
            current = current.children[-1]
        return current.keys[-1]

    def _get_successor(self, x, i):
        current = x.children[i + 1]
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]

    def _fill(self, x, i):
        t = self.t
        if i != 0 and len(x.children[i - 1].keys) >= t:
            self._borrow_from_prev(x, i)
        elif i != len(x.children) - 1 and len(x.children[i + 1].keys) >= t:
            self._borrow_from_next(x, i)
        else:
            if i != len(x.children) - 1:
                self._merge(x, i)
            else:
                self._merge(x, i - 1)

    def _borrow_from_prev(self, x, i):
        child = x.children[i]
        sibling = x.children[i - 1]

        child.keys.insert(0, x.keys[i - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

        x.keys[i - 1] = sibling.keys.pop()

    def _borrow_from_next(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]

        child.keys.append(x.keys[i])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

        x.keys[i] = sibling.keys.pop(0)

    def _merge(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]
        t = self.t

        child.keys.append(x.keys[i])
        child.keys.extend(sibling.keys)

        if not child.leaf:
            child.children.extend(sibling.children)

        x.children.pop(i + 1)
        x.keys.pop(i)

    def traverse(self, x=None, level=0):
        if x is None:
            x = self.root

        # Loga o nível atual e os eventos contidos no nó
        logging.info(f"Nível {level}, {len(x.keys)} eventos:")
        for evento in x.keys:
            logging.info(f"ID: {evento.id_evento}, Nome: {evento.nome}")

        level += 1
        if not x.leaf:
            for child in x.children:
                self.traverse(child, level)
