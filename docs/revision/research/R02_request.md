# 追加調査依頼（統合依頼に含めて送信済み）

対象は博士論文の背景原稿です。既存原稿の参照コミットは 01b50e4a826c635056ea4f6c5fd2774183b5951e です。確認済みの結論と未確認事項を分け、一次資料のURL・DOI・版・節／式／表／図番号、置換文、正確なBibTeXを返してください。

## 5. 調査依頼 R02：背景に追加する物理を、必要な文献へ限定する

**関連編集**：E09、E12、E14。**優先度**：中～高です。

### ChatGPTへ送る依頼文

> 添付原稿にはすでにPeters cycle、Hörandelのpoly-gonato model、Hillasのcomponent B、Berezinskyのdip、Auger2017のankle以上のフィットがあります。これらを重複して説明せず、second kneeをテーマにする博士論文の背景として足りない接続を補ってください。
>
> 以下の候補の本文を必要な箇所だけ確認し、追加銀河成分、逃走による軟化、源近傍の光分解、magnetic horizon、ankle以下の成分の縮退、局所的な源の寄与を整理してください。各項目に、説明する観測量、仮定、現在の原稿へ追記すべき1段落、引用箇所を示してください。全候補を本文で同じ長さに説明する必要はありません。
>
> 全粒子second knee、重成分knee、軽成分ankle、組成の転換、銀河系内外成分の等寄与・移行完了を同一視しないでください。TALE-SDのbreakを特定核種の最大剛性と仮定して計算する場合は、測定結果ではなく条件付きの説明としてください。
>
> 図を追加するなら、既存のHörandel Fig.11では示せない物理を表すものに限り、最多1枚を提案してください。原図を確認し、図番号・版・引用目的を明記します。新しいMCや解析は要求しないでください。

### 探索起点と新規キー案

下記は調査先を特定するリストであり、過去のチャットが作った書誌情報をそのまま確定版として取り込む指示ではありません。

| キー案 | 論文・識別子 | 追記先での役割 |
|---|---|---|
| `Thoudam2016SecondGalactic` | Thoudam et al., A&A595,A33; arXiv:1605.03111; DOI:10.1051/0004-6361/201628894 | 追加銀河成分、組成と全粒子形状 |
| `Giacinti2015Escape` | Giacinti et al., PRD91,083009; arXiv:1502.01608 | 加速限界以外の逃走による説明 |
| `Candia2002Drift` | Candia et al., JHEP12,032; arXiv:astro-ph/0207143 | ドリフトとsecond kneeの歴史的理論 |
| `Mollerach2019Knee` | Mollerach & Roulet, JCAP03,017; arXiv:1812.04026 | 核種別軟化と銀河外成分の接続 |
| `Unger2015SourceEnvironment` | Unger et al., PRD92,123001; arXiv:1505.02153 | 光分解と二次核子 |
| `Auger2023AcrossAnkle` | Auger, JCAP05,024; arXiv:2211.02857 | ankle以下を含むスペクトル・組成の解釈 |
| `Auger2024MagneticHorizon` | Auger, JCAP07,094; DOI:10.1088/1475-7516/2024/07/094 | 磁場と到達時間による抑制 |
| `Fang2026LocalKnee` | Fang & Halzen; arXiv:2601.05435 | 地球近傍のスペクトルと銀河全体の違い |
| `LHAASO2021PeVPhotons` | DOI:10.1038/s41586-021-03498-z | 高エネルギー加速のガンマ線観測 |
| `IceCube2023Galactic` | arXiv:2307.04427; DOI:10.1126/science.adc9818 | 銀河内ハドロン相互作用の別の情報 |

モデルの簡単な説明に不可欠なものを優先してください。文献数を増やすことを目標にしないでください。


## 参照コミットの該当原稿

```tex
全粒子スペクトルは異なる電荷をもつ成分の和である。
加速限界または銀河からの脱出がリジディティ \(\mathcal{R}\) で決まるなら、核種 \(Z\) の折れ曲がりエネルギーは
\begin{equation}
  E_{k,Z}\simeq Z\mathcal{R}_c
  \label{eq:peters_scaling}
\end{equation}
と電荷に比例する。
このため、陽子、ヘリウム、CNO 群、中間質量核、鉄群の各スペクトルが順次急峻化し、質量組成はエネルギーとともに重くなる。
各核種のスペクトルが電荷の順に折れ曲がるこの変化を Peters cycle と呼ぶ~\cite{Peters1961,Horandel2003}。

たとえば、核電荷 \(Z\) をもつ原子核のスペクトルを
\begin{equation}
  J_Z(E)
  =a_Z E^{-\gamma}
  \left[
    1+\left(\frac{E}{Z\mathcal{R}_c}\right)^{\epsilon}
  \right]^{-\Delta\gamma/\epsilon}
  \label{eq:peters_component}
\end{equation}
と書けば、\(E\ll Z\mathcal{R}_c\) では指数 \(\gamma\)、\(E\gg Z\mathcal{R}_c\) では指数 \(\gamma+\Delta\gamma\) となる。
\(\epsilon\) は折れ曲がりの鋭さを表す。
図~\ref{fig:peters_cycle}は、カットオフのエネルギーがリジディティに比例すると仮定した H\"orandel の poly-gonato モデルを示す。
この図では、直接観測から外挿した各質量群のスペクトルを合計し、全粒子スペクトルへ適合している。核電荷の小さい群から順に強度が急減し、knee から second knee に至る構造を作る~\cite{Horandel2003}。
LHAASO の陽子スペクトルに見られる \(3.3\ \mathrm{PeV}\) の急峻化を基準リジディティと仮定すると、鉄に対応するエネルギーは約 \(8.6\times10^{16}\ \mathrm{eV}\) となる。この値は、KASCADE-Grande が報告した電子成分の少ない試料の折れ曲がりと数値的に整合する~\cite{KASCADEGrandeHeavyKnee2011,LHAASOProton2025}。
この対応は Peters cycle の \(Z\) 比例則と整合するが、すべての核種に共通する単一の基準リジディティを示したことにはならない。
ARGO-YBJ/LHAASO 試作機が測定した陽子・ヘリウム成分の折れ曲がりは約 \(0.7\ \mathrm{PeV}\) にあり、LHAASO の陽子スペクトル自体にも傾きの異なる複数の領域があるためである~\cite{ARGOYBJLHAASOLightKnee2015,LHAASOProton2025}。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.92\hsize]{fig/horandel-2003-fig11.pdf}
  \caption{リジディティ依存のカットオフを仮定した poly-gonato モデルによる全粒子スペクトルと質量群別の寄与。左は全質量群でカットオフ後の指数 \(\gamma_c\) を共通とした場合、右は指数変化 \(\Delta\gamma\) を共通とした場合である。凡例の数字は核電荷 \(Z\) の範囲を表す。H\"orandel (2003) の Fig.~11 より引用~\cite{Horandel2003}。}
  \label{fig:peters_cycle}
\end{figure}

核電荷の順に折れ曲がる関係は、その原因が加速限界であっても、銀河磁場からの脱出であっても現れる。
前者では、式~\eqref{eq:hillas_condition}により最大エネルギーは \(Z\) に比例する。後者では、同じリジディティの粒子が同じ拡散係数をもつ。
どちらの機構からも似た全粒子スペクトルが生じるため、その形状だけでは加速限界と銀河磁場からの脱出を識別できない。
核種別スペクトル、\(\langle\ln A\rangle\)、異方性、および近傍 PeVatron が加速できる最高エネルギーを組み合わせれば、折れ曲がりのエネルギーが複数の電荷群で \(Z\) に比例するかを検証できる。
相互作用断面積や粒子生成の変化も空気シャワーの再構成量に影響する。しかし、異なる検出手法で類似の構造が観測されているため、単一の検出器効果だけでは knee 系列を説明できない~\cite{PDGCosmicRays}。
\FloatBarrier

\subsection{Second knee 領域の観測}\label{subsec:second_knee_observations}
宇宙線強度が低い second knee 領域では、直接観測で十分な統計量を得られないため、空気シャワーからエネルギーと質量を推定する。質量の推定値はハドロン相互作用モデルに依存する。
Akeno と Fly's Eye は \((4\)--\(7)\times10^{17}\ \mathrm{eV}\) 付近の緩やかな急峻化を報告した~\cite{AkenoSpectrum1992,FlysEyeSpectrum1994,Horandel2003}。
\(8\times10^{16}\)--\(10^{17}\ \mathrm{eV}\) にも明瞭な構造が測定されており、second knee と呼ばれる特徴エネルギーは解析ごとに異なる。

KASCADE-Grande は観測面積を拡張し、\(10^{16}\)--\(10^{18}\ \mathrm{eV}\) の荷電粒子数とミューオン数を測定した~\cite{KASCADEGrandeDetector2010}。
電子成分が少なく、重い原子核に対応する試料では、
\begin{equation}
  \log_{10}(E/\mathrm{eV})=16.92\pm0.04
\end{equation}
付近に有意な急峻化が見いだされた。この観測は、Peters cycle において鉄など電荷の大きい原子核のスペクトルが急減するという解釈を支持する~\cite{KASCADEGrandeDetector2010,KASCADEGrandeHeavyKnee2011}。
一方、電子成分が多く、軽い原子核に対応する試料では、\(\log_{10}(E/\mathrm{eV})=17.08\pm0.08\) 付近からスペクトルの傾きが緩やかになった~\cite{KASCADEGrandeLightAnkle2013}。
図~\ref{fig:kascade_grande_components}は、近接したエネルギー領域で、重い原子核に対応する試料が急峻化し、軽い原子核に対応する試料では傾きが緩やかになることを示す。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.49\hsize]{fig/kascade-grande-heavy-2011-fig4.pdf}\hfill
  \includegraphics[width=0.49\hsize]{fig/kascade-grande-light-2013-fig5.pdf}
  \caption{KASCADE-Grande が再構成した質量群別エネルギースペクトル。左は全粒子、電子成分の少ない試料、電子成分の多い試料の比較であり、電子成分の少ない試料は約 \(8\times10^{16}\ \mathrm{eV}\) で急峻化する。右では、電子成分の多い試料のスペクトルの傾きが約 \(10^{17.08}\ \mathrm{eV}\) から緩やかになる。左は KASCADE-Grande Collaboration (2011) の Fig.~4、右は同 Collaboration (2013) の Fig.~5 より引用~\cite{KASCADEGrandeHeavyKnee2011,KASCADEGrandeLightAnkle2013}。}
  \label{fig:kascade_grande_components}
\end{figure}

TALE は、低エネルギー側では大気チェレンコフ光、高エネルギー側では大気蛍光を利用し、約 \(2\ \mathrm{PeV}\) から \(2\ \mathrm{EeV}\) までを同じ望遠鏡系で測定した。
そのスペクトルは、\(\log_{10}(E/\mathrm{eV})\simeq16.22\) で傾きが緩やかになり、\(10^{17.1}\ \mathrm{eV}\) 付近で再び急になる。後者が second knee に対応する~\cite{TALESpectrum2018}。
図~\ref{fig:tale_second_knee}では、同一解析のエネルギースケール上で 2 つの折れ曲がりが示されている。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.72\hsize]{fig/tale-spectrum-2018-fig20.pdf}
  \caption{TALE 単眼解析による \(2\ \mathrm{PeV}\) から \(2\ \mathrm{EeV}\) の全粒子エネルギースペクトル。赤線は折れ曲がりを含む適合、灰色帯は系統的不確かさを表す。TALE Collaboration (2018) の Fig.~20 より引用~\cite{TALESpectrum2018}。}
  \label{fig:tale_second_knee}
\end{figure}

Tunka-133 の大気チェレンコフ観測と IceTop/IceCube の地表・氷中同時観測も、PeV から EeV にわたるスペクトルおよび組成変化を測定している~\cite{TunkaSpectrum2020,IceTopComposition2019}。
Pierre Auger Observatory の高密度 \(750\ \mathrm{m}\) 地表アレイは \(10^{17}\ \mathrm{eV}\) 近傍まで閾値を下げ、独立の検出方式で second knee の急峻化を確認した~\cite{AugerSecondKnee2021}。

\begin{table}[htb]
  \centering
  \small
  \caption{Second knee に関係する代表的な観測結果。特徴エネルギーには、各解析のエネルギースケールに固有の系統的不確かさが含まれる。}
  \label{tab:second_knee_results}
  \begin{tabular}{@{}p{0.21\hsize}p{0.24\hsize}p{0.45\hsize}@{}}
    \hline
    実験・解析 & 特徴的エネルギー & 主な観測結果 \\
    \hline
    Akeno・Fly's Eye & \((4\)--\(7)\times10^{17}\ \mathrm{eV}\) & 全粒子スペクトルの緩やかな急峻化を報告~\cite{AkenoSpectrum1992,FlysEyeSpectrum1994} \\
    KASCADE-Grande & \(8.3\times10^{16}\ \mathrm{eV}\) & 電子成分の少ない試料のスペクトルが急峻化~\cite{KASCADEGrandeHeavyKnee2011} \\
    KASCADE-Grande & \(1.2\times10^{17}\ \mathrm{eV}\) & 電子成分の多い試料でスペクトルの傾きが緩やかになる~\cite{KASCADEGrandeLightAnkle2013} \\
    TALE & 約 \(10^{17.1}\ \mathrm{eV}\) & チェレンコフ・蛍光スペクトルに second knee を観測~\cite{TALESpectrum2018} \\
    Pierre Auger & 約 \(10^{17}\ \mathrm{eV}\) & 高密度地表アレイでスペクトルの変曲を確認~\cite{AugerSecondKnee2021} \\
    \hline
  \end{tabular}
\end{table}

表~\ref{tab:second_knee_results}の特徴エネルギーには、露出量、検出効率、エネルギー分解能、蛍光収量、検出器較正、不可視エネルギー補正に由来する不確かさが含まれる。さらに、電子・ミューオン比や \(X_{\max}\) から求める質量組成は、ハドロン相互作用モデルによって変化する。
したがって、second knee の起源は、全粒子スペクトルだけでなく、質量群別スペクトル、\(\langle\ln A\rangle\)、\(X_{\max}\) を同じエネルギー範囲で比較して評価される。

\section{銀河系内外遷移と超高エネルギー宇宙線}
\subsection{銀河系内外遷移のモデル}\label{subsec:galactic_transition}
Second knee から ankle までの遷移を説明するモデルは複数あり、銀河系内成分が急減するエネルギーと、銀河系外成分が優勢になるエネルギーについて異なる予測を与える。
Ankle は Volcano Ranch 実験の John Linsley が 1963 年に初めて報告した。Linsley は同じ論文で、スペクトルの傾きが緩やかになるこの変化を、銀河系内成分と銀河系外成分の交差として解釈している~\cite{LinsleyAnkle1963,DelignyAnkle2014}。
現在、Auger と TA は ankle の位置と形状を大きな露出量で測定している。一方、その原因が銀河系内外成分の交差、対生成 dip、または源から放出される複数成分の重なりのいずれであるかは確定していない~\cite{AugerSpectrum2020,AugerTAEnergyScale2019}。
観測される全粒子強度を
\begin{equation}
  J(E)=J_{\mathrm{G}}(E)+J_{\mathrm{XG}}(E)
\end{equation}
として銀河系内成分と銀河系外成分の和で表すと、折れ曲がりは各成分固有の構造だけでなく、両成分の交差によっても生じる。

\paragraph{銀河系内成分が ankle まで延びるモデル}
このモデルは、標準的な超新星残骸成分より高い最大リジディティをもつ第 2 の銀河成分、いわゆる component B を導入する。銀河系外成分への主な遷移は ankle 付近に置かれる~\cite{Hillas2005}。
この第 2 成分は、EeV 近くまで宇宙線を加速できる銀河系内天体と、陽子から重い原子核までを含む組成を前提とする。
高リジディティ粒子は銀河磁場で強く閉じ込められないため、銀河面方向に予測される異方性の振幅がこのモデルを制約する。

\paragraph{Pair-production dip モデル}
銀河系外陽子は、宇宙マイクロ波背景放射との対生成反応
\begin{equation}
  p+\gamma_{\mathrm{CMB}}\rightarrow p+e^++e^-
\end{equation}
でエネルギーを失う。この過程によって EeV 領域のスペクトルに dip が形成され、その高エネルギー側が ankle として見える~\cite{BerezinskyDip2006}。
この場合、銀河系外陽子は ankle より低いエネルギーから寄与し、銀河系内外遷移は second knee と ankle の間で進む。
明瞭な dip の形成には、銀河系外成分における陽子の優勢が必要である。質量組成の測定は、この条件を直接検証する。

\paragraph{混合組成・低最大リジディティモデル}
陽子から重核までを加速する銀河系外源を考える。最大エネルギーが \(E_{\max,Z}=Z\mathcal{R}_{\max}\) に従うモデルでは、源からの脱出と伝搬中の光核分解によって組成は変化する。
Pierre Auger Observatory の \(5\ \mathrm{EeV}\) 以上のスペクトルと \(X_{\max}\) 分布を一様な源分布で同時適合すると、スペクトル指数の小さい注入スペクトルと比較的低い最大リジディティをもつ解が得られる。ただし、定量的結論は光核反応断面積、源分布、ハドロン相互作用モデルに依存する~\cite{AugerCombinedFit2017}。
この種のモデルでは、源から放出された二次陽子と一次の重い原子核が同じエネルギー領域へ寄与することによっても、ankle の形状が生じる。

以上のモデルは排他的とは限らない。
現実には、複数種の銀河系内源と銀河系外源が同じエネルギー領域へ寄与する場合がある。この場合、second knee、軽い原子核のスペクトルに見られる ankle、全粒子 ankle は異なる遷移段階を表す可能性がある。
全粒子スペクトルに加えて、質量群別スペクトル、\(X_{\max}\) 分布、ミューオン数、銀河座標に対する異方性を同時に再現できるかどうかが、モデルを識別する鍵となる~\cite{PDGCosmicRays,Cristofari2023}。

\subsection{超高エネルギー宇宙線の伝搬と観測}\label{subsec:uhecr_propagation}
銀河系外を伝搬する超高エネルギー宇宙線は、宇宙膨張による断熱損失に加え、背景光子との相互作用でエネルギーと核種を変える。
陽子では電子陽電子対生成に加え、十分高いエネルギーで
\begin{equation}
  p+\gamma_{\mathrm{CMB}}\longrightarrow \Delta^+\longrightarrow
  \begin{cases}
    p+\pi^0,\\
    n+\pi^+
  \end{cases}
\end{equation}
という光パイオン生成が起こる。
Greisen、Zatsepin、Kuzmin は 1966 年、宇宙マイクロ波背景放射との相互作用によって、数十 \(\mathrm{EeV}\) 以上の陽子が遠方から地球へ到達しにくくなることを指摘した~\cite{Greisen1966,ZatsepinKuzmin1966}。
原子核は、宇宙赤外・可視背景放射と宇宙マイクロ波背景放射による光核分解を受け、伝搬中に質量数 \(A\) が減少する~\cite{KoteraOlinto2011}。

予測から約 40 年後の 2008 年、HiRes は GZK カットオフを初めて \(5\sigma\) で観測したと報告した。同じ年、Auger も大統計の地表アレイを用いた独立の測定により、最高エネルギー側で宇宙線強度が急減することを確認した~\cite{HiResGZK2008,AugerSuppression2008}。
現在は Auger と TA がこの急減の形状を精密に測定している~\cite{AugerSpectrum2020,AugerTAEnergyScale2019,PDGCosmicRays}。
しかし、エネルギースペクトルの急減だけでは、伝搬中の GZK 効果と起源天体の最大リジディティを一意に分離できない。
GZK 効果は、宇宙線が伝搬できる距離と近傍宇宙の物質分布に応じて観測結果を変える。一方、最大リジディティが原因であれば、各核種のカットオフは \(Z\) に比例する。質量組成、到来方向、宇宙生成ニュートリノ、\(\gamma\) 線の上限は、両者を識別するための独立した情報を与える。

Auger は 2017 年、\(8\ \mathrm{EeV}\) 以上の大規模双極子異方性を \(5\sigma\) を超える有意度で観測した。双極子の方向は銀河中心と一致せず、このエネルギー領域で銀河系外起源が卓越することを支持する~\cite{AugerDipole2017}。
一方、個々の天体との対応は銀河・銀河間磁場による偏向と限られた統計量のため確立していない~\cite{AugerTA2023ArrivalDirections}。
Auger と TA のスペクトル比較では、各実験のエネルギースケールを系統誤差の範囲内で調整すると、共通視野における一致は改善する。一方、最高エネルギー側には残差がある~\cite{AugerTAEnergyScale2019}。
TA と Auger は主に北天と南天をそれぞれ観測しており、露出とエネルギースケールの違いが最高エネルギー領域の比較に残る~\cite{AugerTAEnergyScale2019}。

低エネルギーから knee 付近までは銀河系内起源が主要と考えられ、超新星残骸の衝撃波、星団風やスーパーバブル、パルサー関連天体などが候補に挙げられる~\cite{Gabici2019,PDGCosmicRays}。超新星残骸で得られる総エネルギーは銀河宇宙線を維持する供給量を満たすが、個々の残骸が陽子を PeV 領域まで加速できるかは未解決である。超高エネルギー \(\gamma\) 線観測は、銀河系内の PeVatron 候補を制約している~\cite{Cao2023}。

Knee から ankle までの \(0.1\)--\(10\ \mathrm{EeV}\) では、銀河系内成分の上限と銀河系外成分の増加が重なる。Ankle model、dip model、混合組成モデルは、この移行が起こるエネルギーと質量組成について異なる予測を与える~\cite{Cristofari2023,PDGCosmicRays}。TALE による \(10^{16.5}\)--\(10^{18.5}\ \mathrm{eV}\) の組成測定は、この領域を直接測定している~\cite{TALEMassComposition2026}。

数 EeV 以上では銀河系外起源が主要と考えられ、約 \(5\ \mathrm{EeV}\) より上の観測結果は重い原子核の寄与を示唆する。候補天体には活動銀河核、電波銀河、ガンマ線バースト、潮汐破壊現象、マグネター、銀河団降着衝撃波、スターバースト銀河などがある~\cite{GlobusBlandford2023}。\(8\ \mathrm{EeV}\) 以上の大規模双極子異方性も銀河系外起源を支持するが、個々の起源天体は同定されていない~\cite{AugerDipole2017,AugerTA2023ArrivalDirections}。

表~\ref{tab:source_by_energy}に、各エネルギー領域の代表的な起源候補と加速条件をまとめる。
\begin{table}[htb]
  \centering
  \small
  \caption{エネルギー領域ごとの代表的な宇宙線起源候補。いずれも確定した対応ではない。}
  \label{tab:source_by_energy}
  \begin{tabular}{@{}p{0.20\hsize}p{0.28\hsize}p{0.25\hsize}p{0.18\hsize}@{}}
    \hline
    エネルギー領域 & 主な起源候補 & 加速・伝搬上の条件 & 状況 \\
    \hline
    \(\mathrm{GeV}\)--\(\mathrm{TeV}\) & 銀河系内の超新星残骸、星形成領域、パルサー関連天体 & 衝撃波加速と銀河内拡散 & 伝搬の影響が大きく、個々の起源天体の同定は難しい \\
    \(\mathrm{TeV}\)--\(\mathrm{PeV}\) & 若い超新星残骸、銀河中心、星団風、スーパーバブル & PeVatron、リジディティに依存する最大エネルギー & 超高エネルギー \(\gamma\) 線観測が候補天体を制約 \\
    \(\mathrm{PeV}\)--\(\mathrm{EeV}\) & 銀河系内起源と銀河系外起源の宇宙線がともに寄与 & knee、second knee、遷移領域 & 組成測定が遷移の起こるエネルギーを制約 \\
    \(\gtrsim 5\ \mathrm{EeV}\) & 活動銀河核、電波銀河、GRB、TDE、マグネター、銀河団衝撃波、スターバースト銀河 & Hillas 条件、損失、脱出、磁場偏向 & 銀河系外起源が有力だが、個々の起源天体は未同定 \\
    \hline
  \end{tabular}
\end{table}

```
