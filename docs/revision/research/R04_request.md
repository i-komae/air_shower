# 追加調査依頼（統合依頼に含めて送信済み）

対象は博士論文の背景原稿です。既存原稿の参照コミットは 01b50e4a826c635056ea4f6c5fd2774183b5951e です。確認済みの結論と未確認事項を分け、一次資料のURL・DOI・版・節／式／表／図番号、置換文、正確なBibTeXを返してください。

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


## 参照コミットの該当原稿

```tex
数世代後には、エネルギーの大部分が電磁成分へ移る。

ただし、ここでの見積もりはエネルギー割合を対象とし、ある深さに存在する粒子数の割合を表さない。
粒子数で見ると、\(\pi^0\to\gamma\gamma\) を起点とする電磁カスケードから大量の \(e^\pm\) と \(\gamma\) が生じ、電磁成分はハドロン成分を大きく上回る。

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

図~\ref{fig:xmax_pdg}に、複数の実験で測定された \(\langle X_{\max}\rangle\) とその揺らぎを示す。
軽い一次粒子は平均的に深い \(X_{\max}\) をもち、重い一次粒子は浅い \(X_{\max}\) をもつ。
また、陽子のような軽い一次粒子では最初の相互作用深さやシャワー発達の揺らぎが大きいため、\(X_{\max}\) 分布の幅も大きくなりやすい。
このため、\(\langle X_{\max}\rangle\) と \(\sigma(X_{\max})\) は、質量組成を推定するための基本的な観測量である~\cite{PDGCosmicRays,TALEMassComposition2026}。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.85\hsize]{fig/Xmax.pdf}
  \caption{\(\langle X_{\max}\rangle\) と \(\sigma(X_{\max})\) のエネルギー依存。PDG のレビュー \textit{Cosmic Rays} の Fig.~30.8 より引用~\cite{PDGCosmicRays}。}
  \label{fig:xmax_pdg}
\end{figure}

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

Heitler--Matthews モデルでは、十分低エネルギーになった荷電パイオンがハドロン相互作用を継続せず、崩壊してミューオンを生成する。
荷電パイオンのエネルギーが臨界エネルギー \(E_\pi^{\mathrm{crit}}\) まで下がると、
各荷電パイオンは 1 個のミューオンを与えると仮定する~\cite{Matthews2005}。

1 世代で荷電パイオンの数は \(N_{\mathrm{ch}}\) 倍になり、
第 \(n\) 世代での各荷電パイオンのエネルギーは
\[
  E_n = \frac{E_0}{N_{\mathrm{tot}}^n}
\]
と近似できる。
崩壊が始まる世代数 \(n_c\) は
\begin{equation}
  \frac{E_0}{N_{\mathrm{tot}}^{n_c}}=E_\pi^{\mathrm{crit}}
\end{equation}
より
\begin{equation}
  n_c = \frac{\ln(E_0/E_\pi^{\mathrm{crit}})}{\ln N_{\mathrm{tot}}}
\end{equation}
である。

このときミューオン数は、その世代での荷電パイオン数に等しいとみなして
\begin{align}
  N_\mu
  &= N_{\mathrm{ch}}^{n_c} \\
  &= \exp\!\left(n_c\ln N_{\mathrm{ch}}\right) \\
  &= \exp\!\left(\ln\!\left(\frac{E_0}{E_\pi^{\mathrm{crit}}}\right)
     \frac{\ln N_{\mathrm{ch}}}{\ln N_{\mathrm{tot}}}\right) \\
  &= \left(\frac{E_0}{E_\pi^{\mathrm{crit}}}\right)^{\beta}
\end{align}
と書ける。
ただし
\begin{equation}
  \beta = \frac{\ln N_{\mathrm{ch}}}{\ln N_{\mathrm{tot}}}
\end{equation}
である。

Matthews の単純モデルと同様に \(N_{\mathrm{ch}}=10\)、\(N_{\mathrm{tot}}=15\) とすると
\[
  \beta = \frac{\ln 10}{\ln 15}\simeq 0.85
\]
が得られる~\cite{Matthews2005}。
この関係から、ミューオン数は
\begin{equation}
  N_\mu \propto E_0^{\beta},
  \qquad
  \beta\simeq 0.85
\end{equation}
となる。指数 \(\beta\) は 1 より小さいため、ミューオン数はエネルギーに比例する場合よりも緩やかに増加する。より現実的な多重度を用いた場合も、\(\beta\) は概ね \(0.85\)--\(0.95\) の範囲にある~\cite{PDGCosmicRays}。

質量数 \(A\) の一次粒子に対しては、直前に導入した重ね合わせモデルを用いる~\cite{Matthews2005,Montanus2013,Stanev2004}。
このときミューオン数は
\begin{align}
  N_\mu^{(A)}(E_0)
  &\simeq A\left(\frac{E_0/A}{E_\pi^{\mathrm{crit}}}\right)^{\beta} \\
  &= A^{1-\beta}\left(\frac{E_0}{E_\pi^{\mathrm{crit}}}\right)^{\beta}
\end{align}
となる~\cite{Matthews2005,Montanus2013}。
同じ全エネルギー \(E_0\) の空気シャワーでは、重い原子核ほどミューオン数が多くなる~\cite{Matthews2005,Montanus2013}。

\subsection{ミューオンパズルと組成解析への影響}\label{subsec:muon_puzzle}
Heitler--Matthews モデルが示すように、地上ミューオン数は一次エネルギーと質量の双方に感度をもつ。
現実の解析では、LHC データを用いて調整したハドロン相互作用モデルを空気シャワーシミュレーションへ外挿する。
しかし、複数の実験では、\(X_{\max}\) などと整合する質量組成を仮定しても、モデル予測が観測されたミューオン量に届かない。
この系統的な不一致をミューオンパズル、または muon deficit problem と呼ぶ~\cite{DembinskiMuon2019,AlbrechtMuonPuzzle2022}。
Auger は 2015 年、ハイブリッド観測から UHECR シャワーの平均ミューオン数を求めた。\(X_{\max}\) と整合する質量組成を仮定しても、観測値は現行モデルの予測を上回った~\cite{AugerMuon2015}。
8 実験による共通尺度のメタ解析は、この不一致が特定の実験だけに現れるのではなく、エネルギーとともに増大することを示した~\cite{DembinskiMuon2019}。

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

このメタ解析によると、約 \(10\ \mathrm{PeV}\) より上では、データと LHC の測定結果に基づいて調整された相互作用モデルとの差がエネルギーとともに増大した。その傾きは EPOS-LHC と QGSJetII-04 の双方に対して有意であった~\cite{DembinskiMuon2019}。
図~\ref{fig:muon_meta_analysis}は、質量組成から期待される \(z_{\mathrm{mass}}\) を差し引いた \(\Delta z=z-z_{\mathrm{mass}}\) が、両モデルに対してエネルギーとともに増加することを示す。

\begin{figure}[htb]
  \centering
  \includegraphics[width=0.92\hsize]{fig/dembinski-muon-2019-fig10.pdf}
  \caption{8 つの空気シャワー実験によるミューオン測定を共通尺度で比較したメタ解析。縦軸は質量組成の期待値を差し引いた \(\Delta z=z-z_{\mathrm{mass}}\)、横軸は一次エネルギーである。左は EPOS-LHC、右は QGSJetII-04 に対する比較を示す。直線は実験内の系統的不確かさの相関を変えた適合であり、KASCADE-Grande と EAS-MSU の点はエネルギースケールを相互較正していない。Dembinski et al. (2019) の Fig.~10 より引用~\cite{DembinskiMuon2019}。}
  \label{fig:muon_meta_analysis}
\end{figure}

Auger の \(6\)--\(16\ \mathrm{EeV}\) のハイブリッド事象では、縦方向発達をデータに合わせても、地表のハドロン由来信号を EPOS-LHC に対して \(1.33\pm0.16\) 倍、QGSJetII-04 に対して \(1.61\pm0.21\) 倍に増やす必要があった~\cite{AugerHadronic2016}。
レビューは、不一致が顕在化するシャワーエネルギーを約 \(40\ \mathrm{PeV}\) と見積もり、これが核子間重心系エネルギー約 \(8\ \mathrm{TeV}\) に対応すると整理している~\cite{AlbrechtMuonPuzzle2022}。
核子間重心系エネルギーが LHC の到達範囲にあっても、空気シャワーでは、加速器実験で十分に制約されていない超前方粒子生成が各世代で繰り返される。このため、衝突エネルギーだけではモデルの信頼性を保証できない。

各ハドロン相互作用から電磁成分へ移るエネルギー割合が減ると、ハドロンカスケードの残存エネルギーは増え、地上のミューオン数も増加する。
候補として、バリオン・反バリオンやストレンジ粒子の生成量、荷電粒子多重度、前方領域の \(\pi^0\) 生成率の修正などが議論されている~\cite{AlbrechtMuonPuzzle2022}。
Heitler--Matthews モデルの関係 \(N_\mu\propto N_{\mathrm{ch}}^{n_c}\) が示すように、1 回の相互作用における小さなエネルギー分配差でも、世代ごとに累積してミューオン数の大きな差となりうる。
ただし、ミューオン数だけを合わせる修正が \(X_{\max}\)、その揺らぎ、地上電磁信号、加速器データを同時に再現するとは限らない。

この問題は second knee の解釈に直接影響する。
```
