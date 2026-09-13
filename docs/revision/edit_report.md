# 原稿改訂の報告

追加調査R01〜R05の回答を取得して原稿へ反映し、利用条件を確認した4図を追加しました。確認できなかった事項の扱いは末尾に明記します。

## 対象と保存状態

対象は main.tex、main.bib、main.pdf です。着手時の HEAD は `01b50e4a826c635056ea4f6c5fd2774183b5951e` で、未コミット変更はありませんでした。原稿改訂を報告した時点では、コミット、プッシュ、環境更新は行っていませんでした。

## 編集項目

| ID | 反映先 | 実施内容 |
|---|---|---|
| E01 | `subsec:cosmic_ray_spectrum` | 正の指数で軟化・硬化を定義し、second knee を単一の値で固定しない導入へ修正しました。 |
| E02 | 宇宙線研究の成立 | 電離測定の細かな数値と装置説明を短縮し、Hess の図と一次文献への引用を維持しました。 |
| E03 | `eq:mean_lnA` | 核種割合による定義と平均質量数の対数との違いを追記しました。F02の平均Xmaxを、既存の推定組成図より前に掲載しました。 |
| E04 | `tab:cosmic_ray_experiments` | 検出器、観測量、換算・較正の列へ再構成しました。非結像型 Tunka、TALE のチェレンコフ光、荷電粒子数と電子数、IceTop の混合信号を区別しました。 |
| E05 | `subsec:fermi_acceleration`, `eq:leaky_box` | 上流・下流の流れを修正し、拡散係数の前にリジディティを定義しました。輸送の単一核種・損失を省く近似を明記しました。 |
| E06 | `subsec:rigidity_larmor`, `eq:peters_scaling`, `eq:peters_component` | エネルギーとリジディティの式に電気素量を含め、V と eV の数値関係とガウス単位系を区別しました。 |
| E07 | `subsec:hillas_condition` | 閉じ込めと有限の加速時間による必要条件を分け、候補天体についての十分条件と読める記述を修正しました。 |
| E08 | `fig:lhaaso_proton_spectrum` | 指数の符号を統一し、三つのべき乗区間と起源成分を区別しました。カットオフ形状についての断定を弱め、ヘリウムの2026年の結果と共通の尺度・補正・模型依存を追加しました。 |
| E09 | `subsec:peters_cycle` | 共通の特徴剛性の仮定、鉄と超重核の終端、モデル曲線と測定の違いを追記しました。Giacintiの逃走モデルとMollerach–Rouletの核種と銀河系外成分の重なりを接続しました。 |
| E10 | `tab:second_knee_results` | 全粒子の位置推定をTALE、KASCADE-Grande、IceTop、Auger SD433で比較し、重・軽成分とXmaxは別表へ分けました。位置固定のSD750と歴史的概数を精密な自由位置推定と混同しないよう修正しました。 |
| E11 | `fig:tale_second_knee`, `fig:tale_lna` | TALE 2018のTable 5の位置・指数・フィット誤差を採用しました。TALE 2026の平均Xmaxの折れ曲がりと推定組成を分けて記述し、F02を追加しました。 |
| E12 | `subsec:galactic_transition` | 出現・等寄与・移行完了を区別しました。Thoudamの追加銀河成分、Ungerの源周囲の光分解、Auger 2023・2024の成分構成と磁場の効果を、適用範囲と仮定を伴って追記しました。 |
| E13 | `subsec:transition_anisotropy` | Auger 2020の測定、双極子ベクトルの合成、上限と位相の解釈、Giacinti 2012の仮定依存の制約を追加しました。Bisterは要旨の範囲に限定しました。F05は転載手続き未了のため掲載していません。 |
| E14 | `tab:source_by_energy` の前後 | Fang–Halzenの局所knee、LHAASOの光子観測、IceCubeの銀河面ニュートリノを追加しました。最初のkneeとsecond knee、拡散放射と未分離源を区別しました。 |
| E15 | `subsec:uhecr_propagation` | 0.1 から 10 EeV の呼称を second knee から ankle 付近へ修正しました。 |
| E16 | `sec:thesis_motivation` | 第1章末に TALE-SD の研究目的を追加しました。未公表結果の数値は追加していません。 |
| E17 | `sec:air_shower_overview`, `subsec:shower_front` | エネルギーの移行を文章で説明し、シャワー前面と時刻分布の幅を区別しました。 |
| E18 | `subsec:heitler_em` | 放射長の定義を修正し、重複する代入を短縮しました。D10 を用い、純電磁モデルの適用範囲を明示しました。 |
| E19 | 重ね合わせモデルと質量組成 | Auger 2013を根拠に質量応答F(E)を放射長から分け、エロンゲーションレートにFの微分項を含めました。係数の評価範囲と検出器応答への注意を明記しました。 |
| E20 | 電子数とミューオン数 | 根拠が確認されていない 0.6 の係数を削除し、粒子定義としきい値に依存する比例関係を残しました。 |
| E21 | `subsec:muon_puzzle` | UMD 2020とSUGAR 2018を追加し、zの検出器応答・平均順序・近似と、陽子仮定による重心系エネルギーを明示しました。F04を追加し、ミューオン密度とS600の倍率を区別しました。 |
| E22 | `subsec:gh` | 長い微分過程を一つの対数微分へ短縮し、定義域・極大・図の各曲線とエネルギー付与との接続を残しました。 |
| E23 | `subsec:fluorescence` | 蛍光とチェレンコフ光を含む再構成、不可視エネルギー、Tunka との違いを修正しました。 |
| E24 | `sec:lateral_structure` | 半径と面密度の面を定義し、傾斜シャワーと密度変化への限定を加えました。AGASA の係数を歴史的な具体例と明記しました。 |
| E25 | `sec:energy_calibration` | CIC、実測較正、MCによる換算、定数補正、信号比とエネルギー残差、スペクトルのヤコビアン、露出と応答を新設節で説明しました。F03を掲載しました。 |

## 導出と図

Heitlerモデルの粒子数・極大深さとGaisser–Hillas関数の微分を、仮定と結論を残して本文内で短縮しました。付録への移動は行っていません。初期観測史の細部を減らし、空気シャワー物理とTALE-SDの測定・較正につながる説明を維持しました。

F01（SD433スペクトル）、F02（TALE Hybridの平均Xmax）、F03（SD433較正）、F04（UMDとXmax）を追加しました。原図の全パネル・軸・凡例を保持し、図の内容は変更していません。原図、抽出結果、組版後の紙面を目視照合しました。既存の13図も実ファイルを描画して確認しました。URL、DOI、版、処理、利用条件は`figure_sources.md`に記載しました。

## 追加調査と文献

利用者の許可後、既存のChatGPTタスクへR01〜R05と関連原稿を送信し、完了した回答を取得しました。別のCodexエージェントへ委任したものではありません。送信本文、回答、識別情報は`research/`に保存しています。

新規文献は17件です。題名・著者・刊行情報を、提示された一次論文やarXivの書誌ページと照合しました。

- `AugerSD4332023`, `AugerAnisotropy2020`, `AugerUMD2020`, `BellidoSUGAR2018`
- `IceTopSpectrum2013`, `LHAASOHelium2026`
- `Thoudam2016SecondGalactic`, `Giacinti2015Escape`, `Mollerach2019Knee`, `Unger2015SourceEnvironment`
- `Auger2023AcrossAnkle`, `Auger2024MagneticHorizon`, `Fang2026LocalKnee`
- `Giacinti2012Transition`, `Bister2026Transition`, `AugerXmaxInterpretation2013`, `IceCubeGalacticPlane2023`

TALE 2018のTable 5（PDF p.17）、KASCADE-Grande 2011（PDF p.4）、IceTop 2013のTable IV（PDF p.10）、ヘリウムのTable S2（v2、PDF p.20）、Dembinski 2019のEq.(4)、Auger 2013のEqs.(2.3)–(2.7)を取得したPDFでも照合しました。SD433、UMD、TALE Hybrid、SUGARの該当本文と図も確認しました。

`Stanev2004`はキーを維持して第2版の刊行年を2010年へ修正しました。既存のarXivリンクと重複したcollaboration表示を修正しました。TALE 2026は新規キーで重複登録していません。

## 未確認事項の扱い

- F05（Auger 2020の異方性図）は原図と両パネルを確認しましたが、当該記事のCC BY表示と必要な転載手続きの完了を確認できないため、本文には掲載していません。測定結果と引用は反映しました。著者への許可申請は行っていません。
- Bister 2026の本文に依存する磁場名、核種群の境界、源の率・寿命、検定の詳細は未確認のため採用していません。要旨に基づく説明であることを本文に明記しました。
- 電子数の係数0.6とTALE 2018の未確認の追加系統誤差は採用していません。
- Tunkaの高い側の位置の自由度・誤差を確認できないため、固定・自由フィットと断定せず概数による形状の報告として扱いました。
- Candiaの詳細や追加の理論図は今回の説明に不可欠ではなく、確認範囲も限られるため追加していません。光子観測の説明には既存のCao 2023を用いました。

## 検証

- 既存の`make pdf`を実行し、終了コード0でPDFを生成しました。`latexmk -f`のためPDFの存在だけでは判断せず、LuaLaTeXとBibTeXの最終ログを確認しました。
- 未定義引用・参照、重複ラベル・引用キー、欠落図、Unicodeや数式のエラーを検査しました。
- 全56ページを描画し、目次、節順、図、キャプション、表、引用、数式の配置を確認しました。比較表の改行と図の配置を調整し、変更の影響を受けるページを再確認しました。
- `git diff --check`で空白上の問題がないことを確認しました。新しい解析、シミュレーション、unfoldingは行っていません。

最終ログは`build/revision/final-build.log`、作業用の描画は`build/revision/qa/`に保存しています。`build/`は既存設定でGitの管理対象外です。
