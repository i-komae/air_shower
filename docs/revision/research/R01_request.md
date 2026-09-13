# 追加調査依頼（統合依頼に含めて送信済み）

対象は博士論文の背景原稿です。既存原稿の参照コミットは 01b50e4a826c635056ea4f6c5fd2774183b5951e です。確認済みの結論と未確認事項を分け、一次資料のURL・DOI・版・節／式／表／図番号、置換文、正確なBibTeXを返してください。

## 4. 調査依頼 R01：second knee比較表の必要部分を確認する

**関連編集**：E08、E10、E11。**優先度**：高いです。対象を以下の未確認箇所に限定し、全実験の再レビューを始めないでください。

### ChatGPTへ送る依頼文

> 日本語の宇宙線博士論文の背景を改訂しています。対象は全粒子second kneeと、組成に関する別の特徴を区別した比較表です。添付の現行段落と引用キーを確認してください。
>
> Auger750の2021年解析はbreak energyを固定しているため、独立した位置測定には数えません。Auger433のPoS(ICRC2023)398については、位置230±50(stat)±35(sys)PeV、幅固定、Fig.4の較正とFig.5のスペクトルを原文で確認済みです。ここを最初から調べ直すのではなく、必要な誤記確認だけ行ってください。
>
> 次を一次論文で確認してください。
> 1. TALE2018 monocularの自由フィット位置、指数、統計・系統の別と表番号。
> 2. KASCADE-Grande2011の全粒子の軟化と、同論文の重成分の軟化を分けた値・有意性・選択条件。2013の軽成分の硬化は別表に置きます。
> 3. IceTop-73 2013の位置がBPLの同時フィットか、区間別べき乗の交点か。2019の組成論文と独立性・役割を区別してください。
> 4. Tunka2020の約3×10^17eVという軟化が、位置と誤差を自由に推定した結果か、概数による形状の記述か。非結像型のQ(200)、MCの換算関係、QUESTによる規格化を確認してください。
> 5. LHAASOの2026年ヘリウム測定を加える場合、陽子との比較に必要な測定量、差し引き手法、尺度の共通性、特徴位置と誤差を確認してください。
>
> 図を目視した値を測定値へ変えないでください。固定した位置は除外しますが、幅だけを固定した解析は位置を自由に推定していれば含めます。主な成果物は、出典位置付きの短い表と、添付原稿への置換段落です。新規の再解析や実験横断フィットを提案する必要はありません。

候補資料は既存の `TALESpectrum2018`、`KASCADEGrandeHeavyKnee2011`、`KASCADEGrandeLightAnkle2013`、`TunkaSpectrum2020`、`IceTopComposition2019` を優先します。追加のIceTop-73は DOI:10.1103/PhysRevD.88.042004、arXiv:1307.3795です。ヘリウムの探索起点はarXiv:2511.05013で、書誌と結果を改めて確認します。


## 参照コミットの該当原稿

```tex

\section{Knee から second knee に至る核種別スペクトル}\label{subsec:knee_observations}
\subsection{全粒子 knee の測定}
Kulikov と Khristiansen は 1958 年、Moscow State University における測定で宇宙線スペクトルの knee を初めて報告した~\cite{KulikovKhristiansen1959,Horandel2003}。
彼らは、空気シャワーの電磁成分から求めたサイズ分布に折れ曲がりを見いだした。
英訳論文は 1959 年に刊行されており、\(10^6\)--\(10^7\) 個の粒子を含むシャワーの領域でサイズ分布の傾きが変化する可能性を論じている~\cite{KulikovKhristiansen1959}。
この観測は一次宇宙線のエネルギースペクトルを核種別に測ったものではなく、電磁成分から求めたシャワーサイズ分布の折れ曲がりであった。
その後、Akeno は電子数とミューオン数から独立に再構成したスペクトルが整合することを示し、\(10^{15.67}\ \mathrm{eV}\) 付近でスペクトル指数が約 2.62 から 3.02 へ変化すると報告した~\cite{AkenoSpectrum1984}。
さらに、異なるシャワー成分を利用し、異なる高度で行われた測定でも類似の急峻化が確認された。これらの一致は、knee が単一検出器の応答変化ではなく、一次宇宙線スペクトルに由来する構造であることを裏付けた~\cite{KASCADEDetector2003,PDGCosmicRays}。

LHAASO-KM2A は 2024 年、\(0.3\)--\(30\ \mathrm{PeV}\) の全粒子スペクトルと \(\langle\ln A\rangle\) を同時に測定した。
折れ曲がりエネルギーは
\begin{equation}
  E_k=3.67\pm0.05_{\mathrm{stat}}\pm0.15_{\mathrm{sys}}\ \mathrm{PeV}
\end{equation}
であり、スペクトル指数はその前後で \(2.7413\) から \(3.128\) へ増加した~\cite{LHAASOKnee2024}。
同解析では \(\langle\ln A\rangle\) が \(0.3\ \mathrm{PeV}\) から約 \(3\ \mathrm{PeV}\) まで減少し、knee より上で増加へ転じた。
この結果は、全粒子 knee におけるスペクトルの急峻化と、陽子など軽い原子核の減少が関係することを示す。ただし、\(\langle\ln A\rangle\) は平均量であるため、knee を作る核種と個々のスペクトルはこの測定だけでは決まらない。
図~\ref{fig:lhaaso_knee_mass}では、全粒子スペクトルの急峻化と \(\langle\ln A\rangle\) の増加への転換が、同じエネルギー領域に現れている。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.56\hsize]{fig/lhaaso-knee-2024-fig3.pdf}
  \caption{LHAASO-KM2A が測定した全粒子エネルギースペクトル（上）と \(\langle\ln A\rangle\)（下）。灰色帯は系統的不確かさ、青線は折れ曲がりを含む適合結果を表す。LHAASO Collaboration (2024) の Fig.~3 より引用~\cite{LHAASOKnee2024}。}
  \label{fig:lhaaso_knee_mass}
\end{figure}

\subsection{陽子・ヘリウム成分と陽子スペクトル}
EAS-TOP は電磁成分とミューオン成分の相関から、knee 付近で重い原子核の割合が増えることを示した。また、ヘリウムのスペクトルが \((3.5\pm0.3)\ \mathrm{PeV}\) 付近で折れ曲がり、全粒子 knee に寄与する可能性を報告した~\cite{EASTOPComposition2004}。
KASCADE は電子数とミューオン数の二次元分布を使い、5 つの質量群に分けてスペクトルを再構成した。その結果、全粒子 knee は主として軽い原子核の減少に由来すると示された~\cite{KASCADEComposition2005}。
ただし、各質量群の絶対強度と折れ曲がりのエネルギーは、シミュレーションに QGSJET と SIBYLL のどちらを用いるかによって異なった。

ARGO-YBJ と LHAASO 広視野チェレンコフ望遠鏡の試作機によるハイブリッド観測は、陽子とヘリウムを合わせたスペクトルが \(0.7\ \mathrm{PeV}\) 付近で急峻化することを 2015 年に報告した~\cite{ARGOYBJLHAASOLightKnee2015}。
この測定では、陽子・ヘリウム成分の折れ曲がりが全粒子 knee より低いエネルギーに現れた。この結果は、同成分が数 PeV まで続くとしたほかの解析とは一致しなかった。
陽子を選別した GRAPES-3 の測定は、\(50\ \mathrm{TeV}\)--\(1.3\ \mathrm{PeV}\) のミューオン多重度分布に基づき、\(166\ \mathrm{TeV}\) 付近でスペクトルの傾きが有意に緩やかになることを示した~\cite{GRAPES3Proton2024}。
この測定の上限は \(1.3\ \mathrm{PeV}\) であり、数 \(\mathrm{PeV}\) における陽子スペクトルの急減は対象外である。一方、陽子スペクトルが knee より低いエネルギーですでに単一のべき乗則から外れることを示している。

LHAASO は 2025 年、電磁粒子数、ミューオン数、チェレンコフ像を同時に用いて、\(0.15\)--\(12\ \mathrm{PeV}\) にわたる高純度陽子試料を同定したと報告した~\cite{LHAASOProton2025}。
陽子純度は \(1\ \mathrm{PeV}\) で約 90\%、エネルギー分解能は \(0.158\ \mathrm{PeV}\) 以上で 15\% 未満と評価されている。
得られたスペクトルには 2 つの折れ曲がりがあり、3 つのべき乗則領域に分かれる。約 \(0.34\ \mathrm{PeV}\) で傾きが緩やかになり、\(3.3\ \mathrm{PeV}\) 付近から急減する。
EPOS-LHC を用いた適合ではスペクトル指数が \(-2.71\) から \(-2.51\)、さらに \(-3.5\) へ変化した。
LHAASO の陽子スペクトルは、\(3\ \mathrm{PeV}\) の単一のカットオフでは記述できない。同研究は、PeV 領域に別の陽子成分が加わる可能性を解釈の 1 つとして示している~\cite{LHAASOProton2025}。
図~\ref{fig:lhaaso_proton_spectrum}は、陽子スペクトルの傾きがいったん緩やかになった後に急になる様子を、強度と局所スペクトル指数によって示している。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.66\hsize]{fig/lhaaso-proton-2025-fig2.pdf}
  \caption{LHAASO が測定した陽子エネルギースペクトル（上）と局所スペクトル指数（下）。赤点は測定値、灰色帯は系統的不確かさを表す。実線は 3 つのべき乗則成分による適合、破線は 2 つのべき乗則成分と指数関数的カットオフによる適合である。LHAASO Collaboration (2025) の Fig.~2 より引用~\cite{LHAASOProton2025}。}
  \label{fig:lhaaso_proton_spectrum}
\end{figure}

\FloatBarrier

\subsection{Peters cycle と knee--second knee の接続}\label{subsec:peters_cycle}
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
```
