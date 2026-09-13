宇宙線の博士論文背景原稿を、添付編集仕様に沿って改訂中です。以下のR01〜R05を追加調査してください。すべて同一改訂の依頼です。一次論文・出版社の資料を用い、必要な主張と出典がそろった時点で回答してください。新たなMC・再解析は不要です。確認済みと未確認を明確にし、各Rごとに出典のURL、DOI、版、式・表・図・ページ、本文用の日本語段落、正確なBibTeXを示してください。原稿はcommit 01b50e4a826c635056ea4f6c5fd2774183b5951eを基に編集しています。

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




## 6. 調査依頼 R03：異方性の新しい研究とBister論文を確認する

**関連編集**：E13。**優先度**：高いです。

### ChatGPTへ送る依頼文

> 博士論文の背景に、銀河系内起源から銀河系外起源への移行を異方性から制約する小節を追加します。Auger2020, ApJ891,142, arXiv:2002.06172のFig.1は、赤道面内の双極子成分の振幅と位相、低エネルギーでの上限を併記する図として確認しています。
>
> Giacinti et al., JCAP07,031(2012), arXiv:1112.5599と、Bister, Oikonomou & Fiorillo, arXiv:2608.26933v1の本文を確認してください。後者はこれまで本文を取得できず、要旨の紹介にとどまっています。要旨から図番号や細部を推測しないでください。
>
> Bister論文について、どのエネルギー・核種群を対象にし、どの源分布、定常／過渡源、銀河磁場、実験データを仮定しているかを整理してください。銀河起源のどのモデルがどの意味で制約されるか、模型を超えて一般化できないことは何かを示してください。second knee付近の重成分、中間質量群、双極子位相の変化を区別してください。
>
> 添付原稿へ追加する日本語の段落案、一次出典の箇所、BibTeXを返してください。模型の予測比較図を追加すると物理的理解が増す場合は最多1枚を、原図の画像を確認して選んでください。Fig.1などの番号を想像で埋めないでください。Auger2020の観測図だけで十分なら、Bisterからの図は不要と明記できます。
>
> 本文をなお取得できなければ、それを明記し、著者要旨だけから書ける限定的な紹介と、確認を要する主張を分けてください。




## 7. 調査依頼 R04：数式・数値係数の根拠を確認する

**関連編集**：E18–E21。**優先度**：高いです。一般的な文章校正ではなく、物理的な断定の確認です。

### ChatGPTへ送る依頼文

> 添付する空気シャワーの説明について、次の4点の根拠を一次資料または標準的な専門書の該当ページで確認してください。
>
> 1. 現稿は純電磁HeitlerモデルのXmaxを陽子のXmaxへ流用した後、質量依存を-X0 lnAとしています。模式的な説明と実際のハドロン模型による質量応答を区別するため、<Xmax>=<Xmax>p-F(E)<lnA>のような表式の出典、仮定、符号を示してください。AugerのXmaxのモーメントとlnAのモーメントを結ぶ研究も探索対象です。
> 2. Ne^max≈0.6(E0/GeV)という現稿の係数について、Stanevの対象版・ページ、電子のしきい値、粒子の定義、対象エネルギーを確認してください。参照DOI10.1007/978-3-540-85148-6は出版社で第2版2010と確認済みですが、本文の係数までは確認できていません。根拠が得られなければ数値の採用を見送り、残せる比例関係と説明を示してください。
> 3. ミューオン指標zでのln< Nmu >と<ln Nmu>、混合組成に対するz_mass≈<lnA>/ln56の近似条件を確認してください。Dembinski2019の式に合わせます。
> 4. 40PeVと核子間重心系約8TeVの対応で、陽子仮定とE/Aの扱いを確認してください。
>
> <lnA>には「平均対数質量」という日本語名を付けず、質量数の自然対数を核種割合で平均した量として説明してください。新しいシミュレーションは不要です。正しい置換文と必要最小限の式、出典位置を返してください。




## 8. 調査依頼 R05：追加図の原図・出典・利用条件を確認する

**関連編集**：F01–F05。**優先度**：図を掲載する前に必要です。

### ChatGPTへ送る依頼文

> 原稿へ以下の図を引用する計画です。図番号とキャプションは一次資料のテキストで確認しましたが、全図の目視確認と再利用条件の確認は未了です。各原図を確認し、ファイル取得元、原図番号・版、パネル、点と線の意味、誤差の種類、本文に必要な限定を返してください。
>
> - Auger433, PoS(ICRC2023)398のFig.5とFig.4。https://pos.sissa.it/444/398/pdf
> - TALE Hybrid, arXiv:2603.14804v1／PRD113,062003のFig.14。既存のFig.22由来のlnA図とは役割を分けます。
> - Auger UMD, EPJC80,751(2020)のFig.12。https://link.springer.com/article/10.1140/epjc/s10052-020-8055-y
> - Auger2020, ApJ891,142、arXiv:2002.06172のFig.1。左右両方を用います。
>
> 公開博士論文への掲載について、出版社または著者が公開している利用条件を調べてください。オープンアクセスやarXivにあることだけで再利用・改変可能とは結論しないでください。PoS資料のCC BY-NC-ND 4.0の表示にも注意します。転載、必要な出典表示、抜き出しや余白処理、改変の可否が不明なら、不明な条件を具体的に示してください。取得していない転載許可を「取得済み」と書かないでください。
>
> 原図と異なる描き直し、点のデジタイズ、新規の概念図を必須としません。出典と図の役割に基づく、日本語キャプション案を返してください。




## 現稿の必要部分（改訂前）

```tex
EPOS-LHC を用いた適合ではスペクトル指数が \(-2.71\) から \(-2.51\)、さらに \(-3.5\) へ変化した。
LHAASO の陽子スペクトルは、\(3\ \mathrm{PeV}\) の単一のカットオフでは記述できない。同研究は、PeV 領域に別の陽子成分が加わる可能性を解釈の 1 つとして示している~\cite{LHAASOProton2025}。
図~\ref{fig:lhaaso_proton_spectrum}は、陽子スペクトルの傾きがいったん緩やかになった後に急になる様子を、強度と局所スペクトル指数によって示している。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.66\hsize]{fig/lhaaso-proton-2025-fig2.pdf}
  \caption{LHAASO が測定した陽子エネルギースペクトル（上）と局所スペクトル指数（下）。赤点は測定値、灰色帯は系統的不確かさを表す。実線は 3 つのべき乗則成分による適合、破線は 2 つのべき乗則成分と指数関数的カットオフによる適合である。LHAASO Collaboration (2025) の Fig.~2 より引用~\cite{LHAASOProton2025}。}
  \label{fig:lhaaso_proton_spectrum}
\end{figure}


```

```tex
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


```

```tex
\subsubsection{重ね合わせモデルと質量組成}
ここで、原子核一次粒子の質量数依存を議論するために、重ね合わせモデルを導入する~\cite{Matthews2005,Montanus2013,Stanev2004}。
この近似では、全エネルギー \(E_0\) をもつ質量数 \(A\) の原子核を、エネルギー \(E_0/A\) をもつ核子 \(A\) 個が同時に入射したものとして扱う。
すなわち、原子核 1 個によるシャワーを、より低いエネルギーの核子シャワー \(A\) 個の重ね合わせとして近似する。

最も単純な近似では、質量数 \(A\) の一次宇宙線による空気シャワーの \(X_{\max}\) は
\[
  X_{\max}^{(A)}(E_0) \simeq X_{\max}^{(p)}\!\left(\frac{E_0}{A}\right)
\]
と書ける。
ここで \(X_{\max}^{(p)}\) は、陽子を一次粒子とする空気シャワーの極大深さである。

式~\eqref{eq:Xmax}を用いると
\[
  X_{\max}^{(p)}(E)=X_0\ln\!\left(\frac{E}{E^\mathrm{crit}}\right)
\]
であるから
\begin{align}
  X_{\max}^{(A)}(E_0)
  &\simeq X_0\ln\!\left(\frac{E_0/A}{E^\mathrm{crit}}\right) \\
  &= X_0\left(\ln\!\left(\frac{E_0}{E^\mathrm{crit}}\right)-\ln A\right) \\
  &= X_{\max}^{(p)}(E_0)-X_0\ln A
\end{align}
となる。
同じ全エネルギー \(E_0\) では、質量数が大きいほど \(X_{\max}\) は \(\ln A\) に比例して浅くなる。

一方、最大粒子数は
\[
  N_{\max}^{(A)}(E_0)
  \simeq A\times \frac{E_0/A}{E^\mathrm{crit}}
  = \frac{E_0}{E^\mathrm{crit}}
\]
となる。
最も単純な近似では、\(N_{\max}\) は質量数に依存しない。

上で導いたように、質量数 \(A\) の一次粒子に対しては
\begin{equation}
  X_{\max}^{(A)}(E_0)
  \simeq X_{\max}^{(p)}(E_0)-X_0\ln A
\end{equation}
である。
一次粒子集団が複数の核種からなり、核種 \(i\) の割合を \(f_i\) とする。ただし、\(f_i\geq0\) かつ \(\sum_i f_i=1\) である。
このとき \(X_{\max}\) の平均は
\begin{align}
  \langle X_{\max}\rangle
  &= \sum_i f_i X_{\max}^{(A_i)}(E_0) \\
  &\simeq \sum_i f_i\left(X_{\max}^{(p)}(E_0)-X_0\ln A_i\right) \\
  &= X_{\max}^{(p)}(E_0)-X_0\sum_i f_i\ln A_i \\
  &= X_{\max}^{(p)}(E_0)-X_0\langle \ln A\rangle
\end{align}
となる。
ここで
\begin{equation}
  \langle \ln A\rangle = \sum_i f_i \ln A_i
\end{equation}
であり、\(\langle\ln A\rangle\) は \(\ln A\) の平均（mean logarithmic mass）を表す。

実際の空気シャワーでは、陽子シャワーの極大深さ \(X_{\max}^{(p)}(E_0)\) は、最初の相互作用深さや粒子生成多重度などの影響を受ける。これらの効果をエネルギー依存の項 \(C(E_0)\) にまとめ、任意の固定した基準エネルギーを \(E_{\mathrm{ref}}\) とすると、模式的に
\begin{equation}
  \langle X_{\max}\rangle
  =
  C(E_0)+X_0\left(\ln\frac{E_0}{E_{\mathrm{ref}}}-\langle \ln A\rangle\right)
\end{equation}
と書ける~\cite{Matthews2005,PDGCosmicRays}。
ここで \(C(E_0)\) はハドロン相互作用モデルに依存し、基準エネルギーの選び方による定数も含む。

平均 \(X_{\max}\) に対するエロンゲーションレートも同様に \(\log_{10}E_0\) に関して定義すると、
\begin{equation}
  D = \frac{\mathrm{d}\langle X_{\max}\rangle}{\mathrm{d}\log_{10}E_0}
\end{equation}
は
\begin{equation}
  D = \frac{\mathrm{d}C}{\mathrm{d}\log_{10}E_0}
  + X_0\left(\ln 10-\frac{\mathrm{d}\langle \ln A \rangle}{\mathrm{d}\log_{10}E_0}\right)
\end{equation}
となる。
エネルギーとともに組成が軽くなる場合は、\(\mathrm{d}\langle\ln A\rangle/\mathrm{d}\log_{10}E_0<0\) である。
このとき、エロンゲーションレート \(D\) は質量組成が一定の場合より大きくなる。
逆に、\(\mathrm{d}\langle\ln A\rangle/\mathrm{d}\log_{10}E_0>0\) なら、組成はエネルギーとともに重くなり、エロンゲーションレートは小さくなる~\cite{Matthews2005,PDGCosmicRays}。

エロンゲーションレートは \(X_{\max}\) のエネルギー依存を通じて質量組成の変化を反映する量である。ただし、\(C(E_0)\) とそのエネルギー依存はハドロン相互作用モデルに依存するため、エロンゲーションレートだけで質量組成を一意に決めることはできない~\cite{Matthews2005,Montanus2013,PDGCosmicRays}。


```

```tex
\subsubsection{電子数とミューオン数}
Heitler モデルでは、電磁シャワーの最大粒子数 \(N_{\max}^{\mathrm{em}}\) は
\[
  N_{\max}^{\mathrm{em}}=\frac{E_0}{E^\mathrm{crit}}
\]
であり、空気中の臨界エネルギー \(E^\mathrm{crit}\simeq 0.08\,\mathrm{GeV}\) を代入すると
\[
  N_{\max}^{\mathrm{em}}\simeq 12.5\,\frac{E_0}{\mathrm{GeV}}
\]
となる。
しかし、Heitler--Matthews モデルでは、エネルギーはまずハドロンカスケードに入り、
各世代でその一部だけが \(\pi^0\) を通じて電磁成分へ移る。
このため、観測される最大電子数は Heitler のモデルよりかなり小さくなる~\cite{Matthews2005,Stanev2004}。

最大電子数については、空気シャワーの経験的な見積もりとして
\begin{equation}
  N_e^{\max}\simeq 0.6\,\frac{E_0}{\mathrm{GeV}}
\end{equation}
が用いられる~\cite{Stanev2004}。
係数はモデルや電子数の定義に依存するが、\(N_e^{\max}\) は \(E_0\) にほぼ比例する。
これは Heitler モデルの \(E_0/E^\mathrm{crit}\) をそのまま使ったものではなく、
ハドロンカスケードを経た後に電磁成分として観測される電子数の半経験的な近似である~\cite{Matthews2005,Montanus2013}。


```

```tex
異なる実験と相互作用モデルを比較するため、平均ミューオン数を
\begin{equation}
  z
  =
  \frac{
    \ln\langle N_\mu\rangle
    -\ln\langle N_{\mu,p}^{\mathrm{MC}}\rangle
  }{
    \ln\langle N_{\mu,\mathrm{Fe}}^{\mathrm{MC}}\rangle
    -\ln\langle N_{\mu,p}^{\mathrm{MC}}\rangle
  }
  \label{eq:muon_z}
\end{equation}
と規格化する方法が用いられる~\cite{DembinskiMuon2019}。
ここで \(N_{\mu,p}^{\mathrm{MC}}\) と \(N_{\mu,\mathrm{Fe}}^{\mathrm{MC}}\) は、それぞれ同じ相互作用モデルによる陽子および鉄シャワーの予測である。
モデルが正しく、組成を陽子から鉄までの範囲に置くと、概ね \(0\leq z\leq 1\) となる。
重ね合わせモデルでは近似的に
\begin{equation}
  z_{\mathrm{mass}}\simeq\frac{\langle\ln A\rangle}{\ln 56}
\end{equation}
であるため、\(X_{\max}\) から得た \(z_{\mathrm{mass}}\) とミューオン観測から得た \(z\) を比較できる。
ミューオンパズルとは、\(X_{\max}\) などで制約された質量組成から期待される値よりも、観測されたミューオン指標が系統的に大きいという不一致である。


```

## 関連する既存書誌情報

```bibtex
@article{TALESpectrum2018,
  author = {{Telescope Array Collaboration}},
  title = {{The Cosmic-Ray Energy Spectrum between 2 PeV and 2 EeV Observed with the TALE Detector in Monocular Mode}},
  journal = {Astrophys. J.},
  volume = {865},
  pages = {74},
  year = {2018},
  doi = {10.3847/1538-4357/aada05}
}
```

```bibtex
@article{TALEMassComposition2026,
  author = {Abbasi, R. U. and others},
  collaboration = {Telescope Array Collaboration},
  title = {{Cosmic ray mass composition measurement in the energy range from $10^{16.5}$ eV to $10^{18.5}$ eV observed with the TALE hybrid detector}},
  journal = {Phys. Rev. D},
  volume = {113},
  pages = {062003},
  year = {2026},
  doi = {10.1103/vrky-dxn7},
  archive = {arXiv},
  eprint = {2603.14804},
  primaryclass = {astro-ph.HE}
}
```

```bibtex
@article{KASCADEGrandeHeavyKnee2011,
  author = {{KASCADE-Grande Collaboration}},
  title = {{Kneelike Structure in the Spectrum of the Heavy Component of Cosmic Rays Observed with KASCADE-Grande}},
  journal = {Phys. Rev. Lett.},
  volume = {107},
  pages = {171104},
  year = {2011},
  doi = {10.1103/PhysRevLett.107.171104}
}
```

```bibtex
@article{KASCADEGrandeLightAnkle2013,
  author = {{KASCADE-Grande Collaboration}},
  title = {{Ankle-like Feature in the Energy Spectrum of Light Elements of Cosmic Rays Observed with KASCADE-Grande}},
  journal = {Phys. Rev. D},
  volume = {87},
  pages = {081101},
  year = {2013},
  doi = {10.1103/PhysRevD.87.081101}
}
```

```bibtex
@article{IceTopComposition2019,
  author = {{IceCube Collaboration}},
  title = {{Cosmic Ray Spectrum and Composition from PeV to EeV Using 3 Years of Data from IceTop and IceCube}},
  journal = {Phys. Rev. D},
  volume = {100},
  pages = {082002},
  year = {2019},
  doi = {10.1103/PhysRevD.100.082002}
}
```

```bibtex
@article{TunkaSpectrum2020,
  author = {{Tunka-133 Collaboration}},
  title = {{The Primary Cosmic-Ray Energy Spectrum Measured with the Tunka-133 Array}},
  journal = {Astropart. Phys.},
  volume = {117},
  pages = {102406},
  year = {2020},
  doi = {10.1016/j.astropartphys.2019.102406}
}
```

```bibtex
@article{AugerSecondKnee2021,
  author = {{Pierre Auger Collaboration}},
  title = {{The Energy Spectrum of Cosmic Rays beyond the Turn-Down around $10^{17}$ eV as Measured with the Surface Detector of the Pierre Auger Observatory}},
  journal = {Eur. Phys. J. C},
  volume = {81},
  pages = {966},
  year = {2021},
  doi = {10.1140/epjc/s10052-021-09700-w}
}
```

```bibtex
@article{LHAASOProton2025,
  author = {{LHAASO Collaboration}},
  title = {{Precise Measurements of the Cosmic Ray Proton Energy Spectrum in the ``Knee'' Region}},
  journal = {Sci. Bull.},
  volume = {70},
  number = {24},
  pages = {4173--4180},
  year = {2025},
  doi = {10.1016/j.scib.2025.10.048}
}
```

```bibtex
@book{Stanev2004,
  author = {Stanev, T.},
  title = {{High Energy Cosmic Rays}},
  edition = {2},
  publisher = {Springer},
  address = {Berlin},
  year = {2004},
  doi = {10.1007/978-3-540-85148-6},
  url = {https://link.springer.com/book/10.1007/978-3-540-85148-6}
}
```

```bibtex
@article{DembinskiMuon2019,
  author = {Dembinski, Hans P. and others},
  title = {{Report on Tests and Measurements of Hadronic Interaction Properties with Air Showers}},
  journal = {EPJ Web Conf.},
  volume = {210},
  pages = {02004},
  year = {2019},
  doi = {10.1051/epjconf/201921002004}
}
```