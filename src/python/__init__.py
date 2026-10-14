"""
EDP - 期望域感知方法 (Expectation Domain Perception Method) V2.0

通用全域概率态势感知框架

EDP 是一个通用的概率预测与决策框架。任何可以被分解为
"若干可能结果 + 若干信息来源" 的问题，都可以用 EDP 处理。

七层堆叠式架构：
    Layer 0: 数据抽象层        (Outcome / Quote / Evidence / Snapshot / EventGraph)
    Layer 1: 概率提取层        (Shin 归一化 / 比例归一化)
    Layer 2: 推断引擎层        (Beta-Binomial / Glicko-2 / 在线聚合 / 在线贝叶斯堆叠)
    Layer 3: 流向分析层        (概率流向 / 动量 / 倍增评分 / 级联检测)
    Layer 4: 全域感知层        (线性池 / 对数优比池 / 贝叶斯累积 / 共识动力学 / 模型多样性)
    Layer 5: 资源分配层        (Kelly / Markowitz / 三原则 / 风险分层)
    Layer 6: 回测与校准层      (Brier / Log / Hyvärinen / CRPS / 校准曲线)
    Layer 7: 保形预测层        (Split Conformal / ACI / AgACI — 2025 前沿)

══════════════════════════════════════════════════════════════════════
⚠️⚠️⚠️ 严重风险警示 ⚠️⚠️⚠️
══════════════════════════════════════════════════════════════════════

本框架仅供学术研究与教育用途。它【不构成】任何投资建议、决策建议、
交易指导或财务规划建议。

1. 概率预测的不确定性：所有概率均为估计值，存在显著不确定性。
2. 历史不代表未来：历史概率模式【不保证】未来结果。
3. 资金损失风险：AllocationEngine 输出可能导致全部本金损失。
4. 模型局限性：框架依赖输入数据质量与各引擎的数学假设。
5. 非专业建议：本框架输出【不是】持牌专业人士的建议。

使用者须自行承担一切决策风险。
══════════════════════════════════════════════════════════════════════

Example:
    >>> from edp import EDP, GenericDomain, Outcome, Evidence
    >>>
    >>> domain = GenericDomain([
    ...     Outcome("a", "结果A"), Outcome("b", "结果B"),
    ... ])
    >>> edp = EDP(domain)
    >>> result = edp.analyze(
    ...     evidence=[
    ...         Evidence("src1", "model", {"probability": 0.7}, confidence=0.8),
    ...         Evidence("src2", "expert", {"probability": 0.65}, confidence=0.6),
    ...     ],
    ...     budget=1000,
    ... )
    >>> print(result["summary"])
"""

from .allocation_engine import (
    AllocationBundle,
    AllocationEngine,
    AllocationLeg,
    AllocationResult,
    RiskTier,
)
from .calibration import (
    CalibrationEngine,
    PredictionRecord,
)
from .conformal import CalibrationRecord as ConformalCalibrationRecord
from .conformal import ConformalConfig, ConformalEngine, PredictionSet
from .core import (
    DomainAdapter,
    EventGraph,
    Evidence,
    GenericDomain,
    Outcome,
    Quote,
    Snapshot,
)
from .domain_awareness import (
    DomainAwarenessEngine,
    EvidenceSource,
    EvidenceType,
    SituationAssessment,
    SourceReliability,
    StabilityLevel,
)
from .edp import EDP
from .flow_amplification import (
    AmplificationLevel,
    AmplificationReport,
    AmplificationResult,
    FlowAmplificationEngine,
)
from .online_aggregator import (
    OnlineAggregator,
    SourcePerformance,
)
from .probability_engine import (
    BayesianPosterior,
    BayesianPrior,
    FlowDirection,
    FlowReport,
    FlowResult,
    Glicko2Rating,
    ProbabilityEngine,
    TrueProbabilityResult,
)

__version__ = "2.0.0"
__author__ = "Nurmamat·Omar"
__license__ = "MIT"

__all__ = [
    # 顶层接口
    "EDP",
    # Layer 0: 数据抽象
    "Outcome",
    "Quote",
    "Evidence",
    "Snapshot",
    "EventGraph",
    "DomainAdapter",
    "GenericDomain",
    # Layer 1-3: 概率引擎
    "FlowDirection",
    "TrueProbabilityResult",
    "BayesianPrior",
    "BayesianPosterior",
    "FlowResult",
    "FlowReport",
    "Glicko2Rating",
    "ProbabilityEngine",
    # Layer 2: 在线聚合
    "OnlineAggregator",
    "SourcePerformance",
    # Layer 3: 流向倍增
    "AmplificationLevel",
    "AmplificationResult",
    "AmplificationReport",
    "FlowAmplificationEngine",
    # Layer 4: 全域感知
    "EvidenceType",
    "SourceReliability",
    "StabilityLevel",
    "EvidenceSource",
    "SituationAssessment",
    "DomainAwarenessEngine",
    # Layer 5: 资源分配
    "RiskTier",
    "AllocationLeg",
    "AllocationResult",
    "AllocationBundle",
    "AllocationEngine",
    # Layer 6: 校准
    "PredictionRecord",
    "CalibrationEngine",
    # Layer 7: 保形预测（2025 前沿）
    "ConformalConfig",
    "ConformalEngine",
    "PredictionSet",
    "ConformalCalibrationRecord",
]
