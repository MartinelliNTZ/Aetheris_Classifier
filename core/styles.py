# -*- coding: utf-8 -*-
"""
Sistema Centralizado de Estilos — Aetheris Classifier v6
=========================================================
Paleta de cores, sombras, gradientes e métodos de estilo QSS.
Toda a identidade visual da aplicacao é controlada aqui.
"""

from __future__ import annotations
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════
# PALETA DE CORES — Teoria: fundo escuro (análogo preto) + acentos dourados
# (complementares ao preto: tons de ouro/warm) + toques azul/verde para info
# ═══════════════════════════════════════════════════════════════════════════

class Palette:
    """Paleta completa com cores base, superfície, texto, acentos e status."""

    # ── Fundos ──────────────────────────────────────────────────────────
    DARK_BG        = "#0D0D0D"      # Fundo mais profundo (quase preto)
    PANEL_BG       = "#1A1A1E"      # Painéis / GroupBox
    CARD_BG        = "#222226"      # Cards / hover / dropdowns
    INPUT_BG       = "#2A2A2E"      # Inputs / campos de texto
    TITLE_BAR_BG   = "#151518"      # Barra de título

    # ── Bordas ──────────────────────────────────────────────────────────
    BORDER         = "#3A3A3E"      # Borda padrão sutil
    BORDER_LIGHT   = "#4A4A4E"      # Borda hover
    BORDER_FOCUS   = "#C9A84C"      # Borda focus (ouro)

    # ── Texto ───────────────────────────────────────────────────────────
    TEXT_PRIMARY   = "#EAEAEA"      # Texto principal (quase branco)
    TEXT_SECONDARY = "#9A9A9E"      # Texto secundário / subtítulo
    TEXT_MUTED     = "#6A6A6E"      # Texto desabilitado / placeholder
    TEXT_GOLD      = "#C9A84C"      # Texto dourado

    # ── Acento Ouro ─────────────────────────────────────────────────────
    GOLD           = "#C9A84C"      # Ouro principal
    GOLD_HOVER     = "#DDBE5A"      # Ouro hover
    GOLD_PRESSED   = "#A88A30"      # Ouro pressionado
    GOLD_GRADIENT_START = "#C9A84C"
    GOLD_GRADIENT_END   = "#B8963A"
    GOLD_LIGHT     = "#E8D08A"      # Ouro claro (brilho)

    # ── Status ──────────────────────────────────────────────────────────
    SUCCESS        = "#4CAF50"      # Verde sucesso
    SUCCESS_HOVER  = "#66BB6A"
    WARNING        = "#FF9800"      # Laranja aviso
    WARNING_HOVER  = "#FFB74D"
    DANGER         = "#E53935"      # Vermelho erro
    DANGER_HOVER   = "#EF5350"
    INFO           = "#42A5F5"      # Azul info
    INFO_HOVER     = "#64B5F6"

    # ── Sombras (box-shadow simuladas com gradientes/cores) ─────────────
    SHADOW_COLOR   = "#080808"
    GLOW_GOLD      = "#C9A84C33"    # Brilho dourado com 20% opacidade
    GLOW_GOLD_HOVER = "#C9A84C44"   # Brilho hover 27%


# ═══════════════════════════════════════════════════════════════════════════
# CLASSE PRINCIPAL DE ESTILOS
# ═══════════════════════════════════════════════════════════════════════════

class AppStyles:
    """Centraliza toda a folha de estilos QSS e métodos auxiliares."""

    # Alias para acesso rapido as cores
    P = Palette

    # ────────────────────────────────────────────────────────────────────
    # QSS GLOBAL — Aplicado via setStyleSheet na aplicacao
    # ────────────────────────────────────────────────────────────────────

    @classmethod
    def global_stylesheet(cls) -> str:
        p = cls.P
        return f"""
        /* ===== GLOBAL ===== */
        QMainWindow, QWidget {{
            background-color: {p.DARK_BG};
            color: {p.TEXT_PRIMARY};
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            font-size: 13px;
        }}

        /* ===== SCROLL AREA ===== */
        QScrollArea {{
            border: none;
            background-color: transparent;
        }}
        QScrollBar:vertical {{
            background: {p.DARK_BG};
            width: 8px;
            margin: 0;
        }}
        QScrollBar::handle:vertical {{
            background: {p.BORDER};
            border-radius: 4px;
            min-height: 30px;
        }}
        QScrollBar::handle:vertical:hover {{
            background: {p.GOLD};
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0;
        }}
        QScrollBar:horizontal {{
            background: {p.DARK_BG};
            height: 8px;
        }}
        QScrollBar::handle:horizontal {{
            background: {p.BORDER};
            border-radius: 4px;
            min-width: 30px;
        }}

        /* ===== GROUP BOX ===== */
        QGroupBox {{
            background-color: {p.PANEL_BG};
            border: 1px solid {p.BORDER};
            border-radius: 10px;
            margin-top: 8px;
            padding: 16px 10px 10px 10px;
            font-weight: 600;
        }}
        QGroupBox::title {{
            subcontrol-origin: padding;
            subcontrol-position: top left;
            left: 4px;
            top: 1px;
            padding: 0 6px;
            color: {p.TEXT_GOLD};
            font-weight: 700;
            font-size: 12px;
            letter-spacing: 0.5px;
            background-color: {p.PANEL_BG};
            border-radius: 4px;
        }}

        /* ===== LABEL ===== */
        QLabel {{
            background: transparent;
            color: {p.TEXT_PRIMARY};
        }}
        QLabel#header_title {{
            font-size: 22px;
            font-weight: 700;
            color: {p.TEXT_PRIMARY};
            letter-spacing: 1px;
        }}
        QLabel#header_subtitle {{
            font-size: 12px;
            color: {p.TEXT_SECONDARY};
        }}
        QLabel#section_badge {{
            background-color: {p.GOLD};
            color: {p.DARK_BG};
            border-radius: 5px;
            padding: 3px 12px;
            font-size: 10px;
            font-weight: 700;
        }}

        /* ===== TITLE BAR ===== */
        QWidget#title_bar {{
            background-color: {p.TITLE_BAR_BG};
            border-bottom: 1px solid {p.BORDER};
        }}
        QLabel#window_title {{
            color: {p.TEXT_SECONDARY};
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.3px;
        }}
        QPushButton#title_btn, QPushButton#title_btn_close {{
            background: transparent;
            color: {p.TEXT_SECONDARY};
            border: none;
            border-radius: 4px;
            min-width: 30px;
            max-width: 30px;
            min-height: 24px;
            max-height: 24px;
            font-size: 12px;
            font-weight: 600;
        }}
        QPushButton#title_btn:hover {{
            background-color: {p.CARD_BG};
            color: {p.TEXT_PRIMARY};
        }}
        QPushButton#title_btn_close:hover {{
            background-color: {p.DANGER};
            color: white;
        }}

        /* ===== LINE EDIT ===== */
        QLineEdit {{
            background-color: {p.INPUT_BG};
            border: 1px solid {p.BORDER};
            border-radius: 6px;
            padding: 4px 8px;
            color: {p.TEXT_PRIMARY};
            selection-background-color: {p.GOLD};
            selection-color: {p.DARK_BG};
        }}
        QLineEdit:focus {{
            border: 1px solid {p.GOLD};
            background-color: {p.CARD_BG};
        }}
        QLineEdit:disabled {{
            background-color: {p.CARD_BG};
            color: {p.TEXT_MUTED};
        }}
        QLineEdit[readOnly="true"] {{
            background-color: {p.CARD_BG};
            color: {p.TEXT_SECONDARY};
        }}

        /* ===== SPIN BOX ===== */
        QSpinBox, QDoubleSpinBox {{
            background-color: {p.INPUT_BG};
            border: 1px solid {p.BORDER};
            border-radius: 6px;
            padding: 3px 8px;
            color: {p.TEXT_PRIMARY};
        }}
        QSpinBox:focus, QDoubleSpinBox:focus {{
            border: 1px solid {p.GOLD};
        }}
        QSpinBox::up-button, QDoubleSpinBox::up-button,
        QSpinBox::down-button, QDoubleSpinBox::down-button {{
            width: 18px;
            background: {p.CARD_BG};
            border-radius: 3px;
            margin: 1px;
        }}
        QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,
        QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {{
            background: {p.GOLD};
        }}

        /* ===== COMBO BOX ===== */
        QComboBox {{
            background-color: {p.INPUT_BG};
            border: 1px solid {p.BORDER};
            border-radius: 6px;
            padding: 3px 8px;
            color: {p.TEXT_PRIMARY};
            min-width: 100px;
        }}
        QComboBox:focus {{
            border: 1px solid {p.GOLD};
        }}
        QComboBox:disabled {{
            background-color: {p.CARD_BG};
            color: {p.TEXT_MUTED};
        }}
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 24px;
            border-left: 1px solid {p.BORDER};
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
        }}
        QComboBox::down-arrow {{
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 6px solid {p.TEXT_SECONDARY};
        }}
        QComboBox QAbstractItemView {{
            background-color: {p.CARD_BG};
            border: 1px solid {p.BORDER};
            border-radius: 4px;
            color: {p.TEXT_PRIMARY};
            selection-background-color: {p.GOLD};
            selection-color: {p.DARK_BG};
            outline: none;
        }}

        /* ===== CHECK BOX ===== */
        QCheckBox {{
            spacing: 8px;
            background: transparent;
            color: {p.TEXT_PRIMARY};
        }}
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
            border-radius: 4px;
            border: 1px solid {p.BORDER};
            background-color: {p.INPUT_BG};
        }}
        QCheckBox::indicator:checked {{
            background-color: {p.GOLD};
            border: 1px solid {p.GOLD};
        }}
        QCheckBox::indicator:hover {{
            border: 1px solid {p.GOLD};
        }}

        /* ===== TABLE ===== */
        QTableWidget {{
            background-color: {p.INPUT_BG};
            border: 1px solid {p.BORDER};
            border-radius: 8px;
            gridline-color: {p.BORDER};
            color: {p.TEXT_PRIMARY};
        }}
        QTableWidget::item {{
            padding: 3px 6px;
            border-bottom: 1px solid {p.BORDER};
        }}
        QTableWidget::item:selected {{
            background-color: {p.GOLD};
            color: {p.DARK_BG};
        }}
        QHeaderView::section {{
            background-color: {p.CARD_BG};
            color: {p.TEXT_SECONDARY};
            padding: 4px 6px;
            border: none;
            border-bottom: 2px solid {p.GOLD};
            font-weight: 700;
            font-size: 11px;
        }}

        /* ===== TEXT BROWSER / TEXT EDIT ===== */
        QTextBrowser, QTextEdit {{
            background-color: {p.INPUT_BG};
            border: 1px solid {p.BORDER};
            border-radius: 8px;
            color: {p.TEXT_PRIMARY};
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 11px;
            padding: 8px;
            selection-background-color: {p.GOLD};
            selection-color: {p.DARK_BG};
        }}

        /* ===== PROGRESS BAR ===== */
        QProgressBar {{
            border: none;
            border-radius: 6px;
            background-color: {p.INPUT_BG};
            text-align: center;
            color: {p.TEXT_PRIMARY};
            font-weight: 700;
            font-size: 12px;
        }}
        QProgressBar::chunk {{
            border-radius: 6px;
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:0,
                stop:0 {p.GOLD_GRADIENT_START},
                stop:1 {p.GOLD_GRADIENT_END}
            );
        }}
        """

    # ────────────────────────────────────────────────────────────────────
    # MÉTODOS AUXILIARES — Estilos inline para widgets específicos
    # ────────────────────────────────────────────────────────────────────

    @classmethod
    def btn_secondary_style(cls) -> str:
        """Botao secundario padrao (config, acoes laterais)."""
        p = cls.P
        return (
            f"QPushButton {{"
            f"  background-color: {p.CARD_BG};"
            f"  color: {p.TEXT_GOLD};"
            f"  border: 1px solid {p.BORDER};"
            f"  border-radius: 6px;"
            f"  padding: 6px 14px;"
            f"  font-weight: 600;"
            f"  font-size: 11px;"
            f"}}"
            f"QPushButton:hover {{"
            f"  background-color: {p.INPUT_BG};"
            f"  border-color: {p.GOLD};"
            f"  color: {p.GOLD_HOVER};"
            f"}}"
            f"QPushButton:pressed {{"
            f"  background-color: {p.DARK_BG};"
            f"}}"
        )

    @classmethod
    def btn_primary_style(cls) -> str:
        """Botao primario (EXECUTAR PIPELINE)."""
        p = cls.P
        return (
            f"QPushButton {{"
            f"  background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"    stop:0 {p.GOLD_GRADIENT_START}, stop:1 {p.GOLD_GRADIENT_END});"
            f"  color: {p.DARK_BG};"
            f"  border: none;"
            f"  border-radius: 6px;"
            f"  padding: 6px 20px;"
            f"  font-weight: 800;"
            f"  font-size: 13px;"
            f"}}"
            f"QPushButton:hover {{"
            f"  background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"    stop:0 {p.GOLD_HOVER}, stop:1 {p.GOLD});"
            f"}}"
            f"QPushButton:pressed {{"
            f"  background: {p.GOLD_PRESSED};"
            f"}}"
            f"QPushButton:disabled {{"
            f"  background-color: {p.CARD_BG};"
            f"  color: {p.TEXT_MUTED};"
            f"  border: 1px solid {p.BORDER};"
            f"}}"
        )

    @classmethod
    def btn_danger_style(cls) -> str:
        """Botao de perigo (CANCELAR)."""
        p = cls.P
        return (
            f"QPushButton {{"
            f"  background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"    stop:0 {p.DANGER}, stop:1 {p.DANGER_HOVER});"
            f"  color: white;"
            f"  border: none;"
            f"  border-radius: 6px;"
            f"  padding: 6px 14px;"
            f"  font-weight: 700;"
            f"  font-size: 11px;"
            f"}}"
            f"QPushButton:hover {{"
            f"  background-color: {p.DANGER_HOVER};"
            f"}}"
            f"QPushButton:pressed {{"
            f"  background-color: #C62828;"
            f"}}"
            f"QPushButton:disabled {{"
            f"  background-color: {p.CARD_BG};"
            f"  color: {p.TEXT_MUTED};"
            f"  border: 1px solid {p.BORDER};"
            f"}}"
        )

    @classmethod
    def btn_ghost_style(cls) -> str:
        """Botao fantasma (adicionar shapefile, listar modelos)."""
        p = cls.P
        return (
            f"QPushButton {{"
            f"  background-color: transparent;"
            f"  color: {p.TEXT_GOLD};"
            f"  border: 1px solid {p.BORDER};"
            f"  border-radius: 5px;"
            f"  padding: 4px 12px;"
            f"  font-weight: 600;"
            f"  font-size: 11px;"
            f"}}"
            f"QPushButton:hover {{"
            f"  background-color: {p.CARD_BG};"
            f"  border-color: {p.GOLD};"
            f"}}"
            f"QPushButton:pressed {{"
            f"  background-color: {p.INPUT_BG};"
            f"}}"
        )

    # ────────────────────────────────────────────────────────────────────
    # ESTILOS DE BADGE
    # ────────────────────────────────────────────────────────────────────

    @classmethod
    def badge_style(cls, bg_color: str, text_color: Optional[str] = None) -> str:
        """Gera estilo QSS para um badge."""
        tc = text_color or cls.P.DARK_BG
        return (
            f"QLabel {{"
            f"  background-color: {bg_color};"
            f"  color: {tc};"
            f"  border-radius: 5px;"
            f"  padding: 3px 12px;"
            f"  font-weight: 700;"
            f"  font-size: 10px;"
            f"}}"
        )

    @classmethod
    def badge_success(cls) -> str:
        return cls.badge_style(cls.P.SUCCESS)

    @classmethod
    def badge_running(cls) -> str:
        return cls.badge_style(cls.P.WARNING)

    @classmethod
    def badge_error(cls) -> str:
        return cls.badge_style(cls.P.DANGER)

    @classmethod
    def badge_canceled(cls) -> str:
        return cls.badge_style(cls.P.WARNING)

    # ────────────────────────────────────────────────────────────────────
    # ESTILOS PARA O CONSOLE (log)
    # ────────────────────────────────────────────────────────────────────

    @classmethod
    def log_html(cls, text: str, timestamp: str,
                 color: str, ts_color: str, weight: str = "400") -> str:
        """Formata uma linha de log em HTML para o QTextBrowser."""
        return (
            f"<span style='color:{ts_color}; font-family:Consolas,\"Courier New\",monospace; "
            f"font-size:11px; font-weight:500;'>[{timestamp}]</span> "
            f"<span style='color:{color}; font-family:Consolas,\"Courier New\",monospace; "
            f"font-size:12px; font-weight:{weight};'>{text}</span>"
        )

    @classmethod
    def log_link_html(cls, text: str, url: str) -> str:
        """Formata um link no console."""
        return (
            f"<span style='color:{cls.P.TEXT_SECONDARY}; "
            f"font-family:Consolas,\"Courier New\",monospace; font-size:12px;'>"
            f"{text}: <a href='{url}' style='color:{cls.P.INFO};'>abrir</a></span>"
        )

    @classmethod
    def log_section_html(cls, text: str) -> str:
        """Formata um cabecalho de secao no console."""
        return (
            f"<span style='color:{cls.P.INFO}; "
            f"font-family:Consolas,\"Courier New\",monospace; font-size:12px; font-weight:600;'>"
            f">{text}</span>"
        )