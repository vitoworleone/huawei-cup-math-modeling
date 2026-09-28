\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{gmcmthesis}[2026/09/26 v5.0 Project layout matching approved chapter 4]
% 本项目正文模板。旧2025版已归档，现行规范见《论文写作与排版规范_以第五版为准.md》。
\DeclareOption{withoutpreface}{}
\DeclareOption{bwprint}{}
\DeclareOption{colorprint}{}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexart}}
\ProcessOptions\relax
\LoadClass[a4paper,cs4size,fontset=none]{ctexart}
\RequirePackage{ifxetex}
\RequireXeTeX
\RequirePackage{geometry,amsmath,amsfonts,amssymb,bm}
\RequirePackage{xcolor,graphicx,tabularx,array,longtable,booktabs,multirow}
\RequirePackage{float,needspace,placeins,indentfirst,caption,enumitem,etoolbox}
\RequirePackage{hyperref}
\geometry{top=25mm,bottom=25mm,left=25mm,right=25mm}
\hypersetup{hidelinks,bookmarksnumbered=true}

% 字体和字号。仅章题顿号使用直斜笔字形，不替换章题汉字字体。
\setmainfont[Path=fonts/,UprightFont=Times-Regular.ttf,BoldFont=Times-Bold.ttf,ItalicFont=Times-Italic.ttf,BoldItalicFont=Times-BoldItalic.ttf]{Times}
\setmonofont[Path=fonts/,UprightFont=Courier-Regular.ttf,BoldFont=Courier-Bold.ttf,ItalicFont=Courier-Italic.ttf,BoldItalicFont=Courier-BoldItalic.ttf]{Courier}
\setsansfont[Path=fonts/,UprightFont=Arial-Regular.ttf,BoldFont=Arial-Bold.ttf,ItalicFont=Arial-Italic.ttf,BoldItalicFont=Arial-BoldItalic.ttf]{Arial}
\setCJKmainfont[Path=fonts/,AutoFakeBold=2.15,ItalicFont={KaiTi.ttf}]{SimSun.ttf}
\setCJKsansfont[Path=fonts/,AutoFakeBold=2.15]{SimHei.ttf}
\setCJKfamilyfont{hei}[Path=fonts/,AutoFakeBold=2.15]{SimHei.ttf}
\setCJKfamilyfont{song}[Path=fonts/,AutoFakeBold=2.15]{SimSun.ttf}
\setCJKfamilyfont{kai}[Path=fonts/]{KaiTi.ttf}
\setCJKfamilyfont{chapterpunct}[Path=fonts/]{TitlePunctuation.ttf}
\providecommand{\heiti}{}
\providecommand{\songti}{}
\providecommand{\kaishu}{}
\renewcommand{\heiti}{\CJKfamily{hei}}
\renewcommand{\songti}{\CJKfamily{song}}
\renewcommand{\kaishu}{\CJKfamily{kai}}
\renewcommand{\baselinestretch}{1}
\setlength{\parindent}{2em}
\setlength{\parskip}{0pt}
\setlength{\emergencystretch}{2em}
\AtBeginDocument{\normalfont\songti\zihao{-4}}
\pagestyle{plain}
\raggedbottom

% 标题编号。章标题“四、问题一……”连续排；小标题编号后0.5em。
\setcounter{secnumdepth}{3}
\renewcommand\thesection{\chinese{section}、}
\renewcommand\thesubsection{\arabic{section}.\arabic{subsection}}
\renewcommand\thesubsubsection{\thesubsection.\arabic{subsubsection}}
\DeclareRobustCommand{\gmcm@titlepunct}{{\mdseries\CJKfamily{chapterpunct}、}\kern-0.5em}
\def\gmcm@sectionnumber{\chinese{section}\gmcm@titlepunct}
\def\gmcm@subsectionnumber{\thesubsection\hspace{0.5em}}
\def\gmcm@subsubsectionnumber{\thesubsubsection\hspace{0.5em}}
\def\@seccntformat#1{\csname gmcm@#1number\endcsname}
\renewcommand\section{\@startsection{section}{1}{\z@}{12pt}{8pt}{\centering\normalfont\heiti\zihao{4}\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}{8pt}{4pt}{\normalfont\songti\zihao{-4}\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}{6pt}{3pt}{\normalfont\songti\zihao{-4}\bfseries}}
\pretocmd{\subsection}{\FloatBarrier}{}{}

% 图、表、公式按章编号。数字章号不受中文章标题影响。
\numberwithin{figure}{section}
\numberwithin{table}{section}
\numberwithin{equation}{section}
\renewcommand{\thefigure}{\arabic{section}-\arabic{figure}}
\renewcommand{\thetable}{\arabic{section}-\arabic{table}}
\renewcommand{\theequation}{\arabic{section}-\arabic{equation}}
\allowdisplaybreaks[1]
\AtBeginDvi{\special{pdf:minorversion 7}}

% 图题在下、表题在上，正常宋体小四；不生成独立“注：”行。
\DeclareCaptionFont{song}{\songti}
\DeclareCaptionFont{minusfour}{\zihao{-4}}
\captionsetup[figure]{format=hang,labelsep=quad,font={normalfont,song,minusfour},position=bottom,width=\textwidth,skip=4pt}
\captionsetup[table]{format=hang,labelsep=quad,font={normalfont,song,minusfour},position=top,skip=4pt}
\setlength{\intextsep}{6pt plus 1pt minus 1pt}
\setlength{\textfloatsep}{8pt plus 1pt minus 1pt}
\setlength{\floatsep}{8pt plus 1pt minus 1pt}
\setlength{\@fptop}{0pt}
\setlength{\@fpsep}{8pt}
\setlength{\@fpbot}{0pt plus 1fil}
\floatplacement{figure}{H}
\floatplacement{table}{H}
\DeclareGraphicsExtensions{.pdf,.png,.jpg}
\graphicspath{{figures/}}

% 三线表统一粗细；表头、数据、合计行均应选用居中列。
\setlength{\heavyrulewidth}{1pt}
\setlength{\lightrulewidth}{0.5pt}
\setlength{\cmidrulewidth}{0.5pt}
\setlength{\tabcolsep}{5pt}
\renewcommand{\arraystretch}{1}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\let\gmcm@oldtabular\tabular
\let\gmcm@endoldtabular\endtabular
\AtBeginEnvironment{table}{\centering\normalfont\songti\zihao{-4}\renewcommand{\arraystretch}{1}}

% 插图辅助命令：等比缩放，宽不超过正文，图题与图保持为一个单元。
\newlength{\gmcm@figurewidth}
\newcommand{\paperfigure}[4][\linewidth]{%
  \begin{figure}[H]\centering
  \setlength{\gmcm@figurewidth}{#1}%
  \ifdim\gmcm@figurewidth>\linewidth\setlength{\gmcm@figurewidth}{\linewidth}\fi
  \includegraphics[width=\gmcm@figurewidth,height=195mm,keepaspectratio]{#2}
  \caption{#3}\label{#4}
  \end{figure}}

% 整篇论文入口可用；当前示例只展示已核定的正文格式，不生成旧年份封面。
\renewcommand{\maketitle}{\begin{center}{\heiti\zihao{3}\bfseries\@title\par}\end{center}}
\renewenvironment{abstract}{\section*{摘要}\normalfont\songti\zihao{-4}}{\par}
\newcommand{\keywords}[1]{\par\noindent\textbf{关键词：}#1\par}
\renewcommand\appendix{\par\setcounter{section}{0}\setcounter{subsection}{0}%
 \gdef\thesection{附录\Alph{section}}%
 \gdef\theHsection{appendix.\Alph{section}}%
 \gdef\gmcm@sectionnumber{\thesection\hspace{0.5em}}%
 \gdef\thesubsection{\Alph{section}.\arabic{subsection}}%
 \gdef\thefigure{\Alph{section}-\arabic{figure}}%
 \gdef\thetable{\Alph{section}-\arabic{table}}%
 \gdef\theequation{\Alph{section}-\arabic{equation}}}
\newcommand{\papercodefont}{\setmonofont[Path=fonts/,UprightFont=Menlo-Regular.ttf,BoldFont=Menlo-Bold.ttf,ItalicFont=Menlo-Italic.ttf,BoldItalicFont=Menlo-BoldItalic.ttf]{Menlo}}
\endinput
