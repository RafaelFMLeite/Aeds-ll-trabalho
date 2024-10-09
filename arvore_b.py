# arvore_b.py

from evento import Evento

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grau minimo
        self.leaf = leaf  # Indica se e uma folha
        self.keys = []  # Lista de chaves (evento_id)
        self.values = []  # Lista de valores (objetos Evento)
        self.children = []  # Lista de filhos

class BTree:
    def __init__(self, t, log_file='arvore_b_log.txt'):
        self.root = BTreeNode(t, True)
        self.t = t  # Grau minimo
        self.log_file = log_file
        # Inicializa o arquivo de log
        with open(self.log_file, 'w') as file:
            file.write("Log da Arvore B\n")
            file.write("================\n")

    def log(self, mensagem):
        with open(self.log_file, 'a') as file:
            file.write(mensagem + "\n")
        print(mensagem)  # Opcional: também imprime no console

    # Funcao de Busca
    def search(self, node, evento_id):
        self.log(f"Iniciando busca pelo Evento ID {evento_id}.")
        i = 0
        while i < len(node.keys) and evento_id > node.keys[i]:
            i += 1
        if i < len(node.keys) and evento_id == node.keys[i]:
            self.log(f"Evento ID {evento_id} encontrado: {node.values[i]}.")
            return node.values[i]
        elif node.leaf:
            self.log(f"Evento ID {evento_id} nao encontrado na arvore.")
            return None
        else:
            self.log(f"Descendo para o filho {i} para continuar a busca.")
            return self.search(node.children[i], evento_id)

    # Funcao para dividir um no cheio durante a insercao
    def split_child(self, parent, i, child):
        t = self.t
        new_node = BTreeNode(t, child.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, child.keys[t - 1])
        parent.values.insert(i, child.values[t - 1])
        self.log(f"Dividindo o no com chaves {[child.keys[j] for j in range(len(child.keys))]}.")
        self.log(f"Movendo a chave {child.keys[t - 1]} para o no pai.")

        # Copia as chaves e valores para o novo no
        new_node.keys = child.keys[t:(2 * t - 1)]
        new_node.values = child.values[t:(2 * t - 1)]
        child.keys = child.keys[:t - 1]
        child.values = child.values[:t - 1]

        if not child.leaf:
            new_node.children = child.children[t:(2 * t)]
            child.children = child.children[:t]

    # Funcao para inserir uma nova chave na arvore
    def insert(self, evento):
        self.log(f"Solicitacao de insercao do Evento ID {evento.evento_id}.")

        # Verificar se o evento_id já existe
        if self.search(self.root, evento.evento_id) is not None:
            self.log(f"Insercao negada: Evento ID {evento.evento_id} ja existe na arvore.")
            print(f"Erro: Evento ID {evento.evento_id} ja existe. Insercao negada.")
            return  # Negar a insercao

        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            self.log("A raiz esta cheia. Dividindo a raiz.")
            new_node = BTreeNode(self.t, False)
            new_node.children.append(self.root)
            self.split_child(new_node, 0, self.root)
            self._insert_non_full(new_node, evento)
            self.root = new_node
        else:
            self._insert_non_full(root, evento)

    # Funcao auxiliar para inserir em um no que nao esta cheio
    def _insert_non_full(self, node, evento):
        i = len(node.keys) - 1
        if node.leaf:
            # Insere diretamente em um no folha
            node.keys.append(None)
            node.values.append(None)
            while i >= 0 and evento.evento_id < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                node.values[i + 1] = node.values[i]
                i -= 1
            node.keys[i + 1] = evento.evento_id
            node.values[i + 1] = evento
            self.log(f"Evento ID {evento.evento_id} inserido no no folha com chaves agora: {node.keys}.")
        else:
            # Insere em um no interno
            while i >= 0 and evento.evento_id < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.log(f"O filho {i} com chaves {[node.children[i].keys[j] for j in range(len(node.children[i].keys))]} esta cheio. Dividindo.")
                self.split_child(node, i, node.children[i])
                if evento.evento_id > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], evento)

    # Funcao para remover uma chave
    def remove(self, evento_id):
        self.log(f"Solicitacao de remocao do Evento ID {evento_id}.")
        self._remove(self.root, evento_id)
        # Se a raiz ficar vazia apos a remocao, ajusta a arvore
        if len(self.root.keys) == 0:
            if not self.root.leaf:
                self.log("A raiz ficou vazia. Ajustando a raiz para o primeiro filho.")
                self.root = self.root.children[0]
            else:
                self.log("A raiz ficou vazia e e uma folha. A arvore esta vazia.")
                self.root = BTreeNode(self.t, True)

    # Funcao auxiliar para remover
    def _remove(self, node, evento_id):
        t = self.t
        i = 0
        while i < len(node.keys) and evento_id > node.keys[i]:
            i += 1
        if i < len(node.keys) and evento_id == node.keys[i]:
            self.log(f"Evento ID {evento_id} encontrado no no com chaves {node.keys}.")
            if node.leaf:
                node.keys.pop(i)
                node.values.pop(i)
                self.log(f"Evento ID {evento_id} removido do no folha. Chaves restantes: {node.keys}.")
            else:
                self._remove_internal_node(node, evento_id, i)
        elif node.leaf:
            self.log(f"Evento ID {evento_id} nao encontrado na arvore.")
            return
        else:
            flag = (i == len(node.keys))
            if len(node.children[i].keys) < t:
                self._fill(node, i)
            if flag and i > len(node.keys):
                self._remove(node.children[i - 1], evento_id)
            else:
                self._remove(node.children[i], evento_id)

    # Funcao auxiliar para remover de um no interno
    def _remove_internal_node(self, node, evento_id, idx):
        t = self.t
        if len(node.children[idx].keys) >= t:
            pred = self._get_predecessor(node, idx)
            self.log(f"Substituindo o Evento ID {evento_id} pelo predecessor {pred.evento_id}.")
            node.keys[idx] = pred.evento_id
            node.values[idx] = pred
            self._remove(node.children[idx], pred.evento_id)
        elif len(node.children[idx + 1].keys) >= t:
            succ = self._get_successor(node, idx)
            self.log(f"Substituindo o Evento ID {evento_id} pelo sucessor {succ.evento_id}.")
            node.keys[idx] = succ.evento_id
            node.values[idx] = succ
            self._remove(node.children[idx + 1], succ.evento_id)
        else:
            self.log(f"Mesclando os filhos {idx} e {idx + 1} porque ambos possuem menos que {t} chaves.")
            self._merge(node, idx)
            self._remove(node.children[idx], evento_id)

    # Funcoes auxiliares para obter predecessor e sucessor
    def _get_predecessor(self, node, idx):
        current = node.children[idx]
        while not current.leaf:
            current = current.children[-1]
        return current.values[-1]

    def _get_successor(self, node, idx):
        current = node.children[idx + 1]
        while not current.leaf:
            current = current.children[0]
        return current.values[0]

    # Funcao auxiliar para preencher um filho com menos que t chaves
    def _fill(self, node, idx):
        t = self.t
        if idx != 0 and len(node.children[idx - 1].keys) >= t:
            self._borrow_from_prev(node, idx)
        elif idx != len(node.children) - 1 and len(node.children[idx + 1].keys) >= t:
            self._borrow_from_next(node, idx)
        else:
            if idx != len(node.children) - 1:
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    # Funcoes auxiliares para emprestar chaves
    def _borrow_from_prev(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx - 1]
        child.keys.insert(0, node.keys[idx - 1])
        child.values.insert(0, node.values[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        node.keys[idx - 1] = sibling.keys.pop()
        node.values[idx - 1] = sibling.values.pop()
        self.log(f"Emprestando uma chave do irmão a esquerda. Chaves do no atual: {child.keys}.")

    def _borrow_from_next(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys[idx])
        child.values.append(node.values[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        node.keys[idx] = sibling.keys.pop(0)
        node.values[idx] = sibling.values.pop(0)
        self.log(f"Emprestando uma chave do irmão a direita. Chaves do no atual: {child.keys}.")

    # Funcao auxiliar para mesclar dois filhos
    def _merge(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys.pop(idx))
        child.values.append(node.values.pop(idx))
        child.keys.extend(sibling.keys)
        child.values.extend(sibling.values)
        if not child.leaf:
            child.children.extend(sibling.children)
        node.children.pop(idx + 1)
        self.log(f"Filhos mesclados. Novo no com chaves: {child.keys}.")

    # Funcao para visualizar a arvore
    def print_tree(self, node, nivel=0):
        indent = "    " * nivel
        self.log(f"{indent}Nivel {nivel} - Chaves: {node.keys}")
        for child in node.children:
            self.print_tree(child, nivel + 1)
