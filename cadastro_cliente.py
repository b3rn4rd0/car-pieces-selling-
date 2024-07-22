import sys
from PyQt6 import QtWidgets, QtCore, QtGui, QtSql
 
class CadastroCliente(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
   
    def setupUi(self):
        self.setWindowTitle("Cadastro de Cliente")
        self.setGeometry(100, 100, 400, 300)
 
        # Layout principal
        self.layout = QtWidgets.QVBoxLayout(self)
 
        # Nome
        self.label_nome = QtWidgets.QLabel("Nome:")
        self.layout.addWidget(self.label_nome)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.lineEdit_4)
 
        # Senha
        self.label_senha = QtWidgets.QLabel("Senha:")
        self.layout.addWidget(self.label_senha)
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.lineEdit_5)
 
        # Email
        self.label_email = QtWidgets.QLabel("Email:")
        self.layout.addWidget(self.label_email)
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.lineEdit_6)
 
        # Data de Nascimento
        self.label_data_nascimento = QtWidgets.QLabel("Data de Nascimento:")
        self.layout.addWidget(self.label_data_nascimento)
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setCalendarPopup(True)
        self.layout.addWidget(self.dateEdit)
 
        # Tipo de Usuário
        self.label_tipo_usuario = QtWidgets.QLabel("Tipo de Usuário:")
        self.layout.addWidget(self.label_tipo_usuario)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItems(["Cliente", "Fornecedor"])
        self.layout.addWidget(self.comboBox)
 
        # Botão de Cadastro
        self.pushButton_4 = QtWidgets.QPushButton("Cadastrar", self)
        self.layout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.cadastrar_usuario)
 
    def cadastrar_usuario(self):
        nome = self.lineEdit_4.text()
        senha = self.lineEdit_5.text()
        email = self.lineEdit_6.text()
        data_nascimento = self.dateEdit.date().toString("yyyy-MM-dd")
        tipo_usuario = self.comboBox.currentText()
 
        # Validação dos campos
        if not nome or not senha or not email:
            QtWidgets.QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return
 
        # Conexão com o banco de dados MySQL
        try:
            banco = QSqlDatabase.addDatabase("QMYSQL")
            banco.setHostName("localhost:3307")
            banco.setDatabaseName("projetooficina")
            banco.setUserName("bernardo")
            banco.setPassword("argentina")
            ok = banco.open()
            conexao = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="projetooficina"
            )
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nome, senha, email, data_nascimento, tipo_usuario) VALUES (%s, %s, %s, %s, %s)",
                (nome, senha, email, data_nascimento, tipo_usuario)
            )
            conexao.commit()
            QtWidgets.QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso.")
            conexao.close()
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao conectar ao banco de dados: {err}")
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cadastro = CadastroCliente()
    cadastro.show()
    sys.exit(app.exec())
