from sqlalchemy import Column, Integer, String, Date, DateTime, Float, text
from .db import Base
from .crud import CRUDMixin

class TarefasTable(Base, CRUDMixin):
    __tablename__ = 'tarefas_table'
    __table_args__ = {'schema': 'autokit'}
    
    # fillable = ['situacao','cor','responsavel','data_cadastro','carteira','data_situacao','uf_juizo','data_integracao','prazo_final','pasta_id','pasta','subpasta','data_lancamento','prazo_interno','solicitante','evento','duracao','publico','origem_informacao','modelo_tarefa','data_inicio_contagem','dias_ate_prazo_final','lancamento_conferido','terceiro','data_protocolo','unidade','importado','usuario_atualizacao','data_atualizacao','juizo','numero_processo','numero_processo_unificado','tipo_evento','conferencia_situacao','prazo_final_hora','local_tarefa','classificacao','motivo_situacao_ultima_solicitacao','tag_controle','sentenca_ou_acordao','valor_alcada','valor_acordo','valor_contraproposta','valor_dano_moral','valor_dano_material','valor_sentenca','motivo_situacao_ultima_aprovacao']

    id = Column(Integer, primary_key=True, nullable=False)
    situacao = Column(String(15), nullable=True)
    cor = Column(String(15), nullable=True)
    responsavel = Column(String(80), nullable=True)
    data_cadastro = Column(Date, nullable=True)
    carteira = Column(String(35), nullable=True)
    data_situacao = Column(DateTime, nullable=True)
    uf_juizo = Column(String(2), nullable=True)
    data_integracao = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=True)
    prazo_final = Column(DateTime, nullable=True)
    pasta_id = Column(Integer, nullable=True)
    pasta = Column(Integer, nullable=True)
    subpasta = Column(Integer, nullable=True)
    data_lancamento = Column(DateTime, nullable=True)
    prazo_interno = Column(DateTime, nullable=True)
    solicitante = Column(String(80), nullable=True)
    evento = Column(String(70), nullable=True)
    duracao = Column(String(10), nullable=True)
    publico = Column(String(5), nullable=True)
    origem_informacao = Column(String(25), nullable=True)
    modelo_tarefa = Column(String(25), nullable=True)
    data_inicio_contagem = Column(DateTime, nullable=True)
    dias_ate_prazo_final = Column(Integer, nullable=True)
    lancamento_conferido = Column(String(5), nullable=True)
    terceiro = Column(String(75), nullable=True)
    data_protocolo = Column(DateTime, nullable=True)
    unidade = Column(String(15), nullable=True)
    importado = Column(String(5), nullable=True)
    usuario_atualizacao = Column(String(75), nullable=True)
    data_atualizacao = Column(DateTime, nullable=True)
    juizo = Column(String(50), nullable=True)
    numero_processo = Column(String(60), nullable=True)
    numero_processo_unificado = Column(String(60), nullable=True)
    tipo_evento = Column(String(100), nullable=True)
    conferencia_situacao = Column(String(100), nullable=True)
    prazo_final_hora = Column(String(10), nullable=True)
    local_tarefa = Column(String(100), nullable=True)
    classificacao = Column(String(60), nullable=True)
    motivo_situacao_ultima_solicitacao = Column(String(200), nullable=True)
    tag_controle = Column(String(200), nullable=True)
    sentenca_ou_acordao = Column(String(150), nullable=True)
    valor_alcada = Column(Float, nullable=True)
    valor_acordo = Column(Float, nullable=True)
    valor_contraproposta = Column(Float, nullable=True)
    valor_dano_moral = Column(Float, nullable=True)
    valor_dano_material = Column(Float, nullable=True)
    valor_sentenca = Column(Float, nullable=True)
    motivo_situacao_ultima_aprovacao = Column(String(200), nullable=True)





