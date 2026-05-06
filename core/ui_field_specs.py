from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class FieldValueType(str, Enum):
    PATH = "path"
    STR = "str"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"


@dataclass(frozen=True)
class UIFieldSpec:
    label: str
    default: object
    description: str
    type: FieldValueType


UI_FIELD_SPECS: dict[str, UIFieldSpec] = {
    "training_image": UIFieldSpec(
        label="Imagem Treino",
        default="dados/imagemTreino.tif",
        description="Raster usado para extrair amostras e treinar o modelo supervisionado conforme shapefiles cadastrados.",
        type=FieldValueType.PATH,
    ),
    "classification_image": UIFieldSpec(
        label="Imagem Classif.",
        default="dados/imagemCompleta.tif",
        description="Raster completo que sera processado pelo modelo para gerar o mapa classificado final.",
        type=FieldValueType.PATH,
    ),
    "output_tiff": UIFieldSpec(
        label="Saida GeoTIFF",
        default="resultado/mapa_classificado_ui.tif",
        description="Arquivo GeoTIFF de saida com classes previstas para cada pixel valido da imagem.",
        type=FieldValueType.PATH,
    ),
    "hidden_layers": UIFieldSpec(
        label="Camadas Ocultas",
        default="128, 64, 32",
        description="Lista de neuronios por camada densa, separada por virgulas, para arquitetura da rede.",
        type=FieldValueType.STR,
    ),
    "activation": UIFieldSpec(
        label="Ativacao",
        default="relu",
        description="Funcao de ativacao aplicada nas camadas ocultas para introduzir nao linearidade no treinamento.",
        type=FieldValueType.STR,
    ),
    "dropout_rate": UIFieldSpec(
        label="Dropout",
        default=0.1,
        description="Percentual de neuronios desligados durante treino para reduzir overfitting e melhorar generalizacao.",
        type=FieldValueType.FLOAT,
    ),
    "epochs": UIFieldSpec(
        label="Epocas",
        default=150,
        description="Quantidade de passagens completas no conjunto de treino durante ajuste dos pesos.",
        type=FieldValueType.INT,
    ),
    "batch_size_train": UIFieldSpec(
        label="Batch Treino",
        default=64,
        description="Numero de amostras por lote no treinamento; valores maiores usam mais memoria.",
        type=FieldValueType.INT,
    ),
    "batch_size_pred": UIFieldSpec(
        label="Batch Predicao",
        default=4096,
        description="Tamanho do batch para predicao no raster completo, ajustado conforme memoria disponivel.",
        type=FieldValueType.INT,
    ),
    "test_size": UIFieldSpec(
        label="Test Size (%)",
        default=0.30,
        description="Fracao separada para validacao e metricas durante treino supervisionado do classificador.",
        type=FieldValueType.FLOAT,
    ),
    "random_state": UIFieldSpec(
        label="Random State",
        default=42,
        description="Semente aleatoria para reproducibilidade na divisao de dados e resultados de treinamento.",
        type=FieldValueType.INT,
    ),
    "ram_limit_pct": UIFieldSpec(
        label="Limite RAM (%)",
        default=70,
        description="Percentual maximo de RAM permitido para processamento do pipeline e predicao por chunks.",
        type=FieldValueType.INT,
    ),
    "use_mask": UIFieldSpec(
        label="Usar mascara (ultima banda = alpha)",
        default=True,
        description="Usa a banda alpha para decidir pixels validos quando o raster possui banda de mascara.",
        type=FieldValueType.BOOL,
    ),
    "zero_as_nodata": UIFieldSpec(
        label="Valores zerados como nodata",
        default=False,
        description="Quando habilitado, pixels com todas as bandas zeradas sao tratados como nodata automaticamente.",
        type=FieldValueType.BOOL,
    ),
    "nodata_threshold": UIFieldSpec(
        label="Limiar Nodata",
        default=250,
        description="Limiar multibanda para marcar nodata quando todas as bandas excedem o valor definido.",
        type=FieldValueType.INT,
    ),
    "model_action": UIFieldSpec(
        label="Acao do Modelo",
        default="Treinar modelo novo",
        description="Define se o pipeline treina modelo novo, retreina existente ou apenas classifica.",
        type=FieldValueType.STR,
    ),
    "existing_model_path": UIFieldSpec(
        label="Modelo Existente",
        default="",
        description="Caminho do arquivo .keras usado nas opcoes de retreinamento ou classificacao direta.",
        type=FieldValueType.PATH,
    ),
    "save_model": UIFieldSpec(
        label="Salvar modelo treinado em disco (.keras)",
        default=True,
        description="Salva o modelo treinado com timestamp para reutilizacao futura sem novo treinamento.",
        type=FieldValueType.BOOL,
    ),
    "model_path": UIFieldSpec(
        label="Caminho do Modelo",
        default="resultado/modelo_ui.keras",
        description="Nome base usado para salvar arquivo do modelo treinado no formato Keras.",
        type=FieldValueType.PATH,
    ),
}
