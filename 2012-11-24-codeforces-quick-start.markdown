Title: Codeforces 快速入門
Date: 2012-11-24
Tags: Algorithm
Author: 張昱珩 (Chang Yu-heng)

1. 什麼是 [Codeforces](http://codeforces.com/)？

    Codeforces 是一個知名的程式競賽 (programming contest) 網站。我們可以在此網站上討論程式設計，練習或比賽解題，也可以舉辦比賽。

2. 支援哪些語言？

    * C
    * C++
    * C#
    * Delphi
    * Free Pascal
    * Haskell
    * Java
    * OCaml
    * PHP
    * Python
    * Ruby
    * Scala

3. 怎麼開始？

    1. 註冊

        1. 進入 [Codeforces](http://codeforces.com/) 首頁

        2. 點選右上角「Register」以進入註冊頁面

            [![](http://4.bp.blogspot.com/-XfEvaDBCOTk/ULM8IT2DcXI/AAAAAAAAACs/c1h6HPfQEyU/s1600/begin_to_register.png)](http://4.bp.blogspot.com/-XfEvaDBCOTk/ULM8IT2DcXI/AAAAAAAAACs/c1h6HPfQEyU/s1600/begin_to_register.png)

        3. 填寫註冊表單，完成後按下「Register (確定註冊)」

            [![](http://1.bp.blogspot.com/-llYPYqqCEdA/ULM_auEZaQI/AAAAAAAAADM/95hG-xkdYuo/s1600/registration_form.png)](http://1.bp.blogspot.com/-llYPYqqCEdA/ULM_auEZaQI/AAAAAAAAADM/95hG-xkdYuo/s1600/registration_form.png)

        經過以上步驟即可完成註冊。

        以下為選擇性設定：

        1. 登入

        2. 點選右上角自己的帳號，進入個人資料頁面

        3. 點選導覽列上的「SETTINGS」

        4. 在「GENERAL」這一頁，可以上傳個人頭像、重新設定密碼、電子信箱等

        5. 在「SOCIAL」這一頁，可以輸入真名及國家和城市。(有輸入國家和城市才能和自己國家的國民一起排名)

    2. 進行一次練習

        1. 解題

            1. 點選導覽列上的 [PROBLEMSET](http://codeforces.com/problemset) 進入考古題庫

            2. 點選最右邊的欄位標題「[Solved](http://codeforces.com/problemset?order=BY_SOLVED_DESC)」

            3. 進入「[Theater Square](http://codeforces.com/problemset/problem/1/A)」

            [![](http://2.bp.blogspot.com/-6Ci3mHL_wD4/ULNiXNDzf6I/AAAAAAAAADc/KnH3HOrCPS8/s1600/problemset.png)](http://2.bp.blogspot.com/-6Ci3mHL_wD4/ULNiXNDzf6I/AAAAAAAAADc/KnH3HOrCPS8/s1600/problemset.png)

            題目最上方的：

                :::text
                time limit per test: 2 seconds
                memory limit per test: 64 megabytes
                input: standard input
                output: standard output

            分別表示：

                :::text
                時間限制：2 秒
                使用記憶體大小限制：64 MB
                輸入方式：標準輸入
                輸出方式：標準輸出

            接著是題目：

                :::text
                Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

                What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered.
                It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

            中文大意：

                :::text
                有一塊&nbsp;n × m (長 n，寬 m) 平方公尺矩形的地需要舖滿石磚，每塊石磚大小為正方形&nbsp;a × a。在不切割石磚、不重疊石的前題下，必需舖滿此地。石磚可以超出需要被舖的地，但石磚的邊必需與此地的邊平行。

                請問最少需要多少石磚才能完成？

            Input (說明測試程式會餵給我們的程式的資料)：

                :::text
                The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 10^9).

            中文說明：

                :::text
                輸入共一行，此行中包含三個整數：n, m, a，整數間以空白字元分隔。其中 1 ≤  n, m, a ≤ 10^9。

            Output (說明我們的程式應該輸出什麼)：

                :::text
                Write the needed number of flagstones.

            中文說明：

                :::text
                請輸出需要的石磚數。

            範例：

            Input:

                :::text
                6 6 4

            Output

                :::text
                4

            註：

                第一個 6 表示 n，第二個 6 表示 m，4 表示 a。亦即，在 6 × 6 大小的地上，舖以 4 × 4 大小的石磚，最少需要 4 塊石磚才能將其舖滿。

            題解：

                假設需要 p × q 塊石磚，其必需符合此條件：a × p ≥ m 且 a × q ≥ n。

            將我們的解法用程式寫出來，並上傳到 Codeforces 即完成此題練習。

        2. 上傳

            在題目頁點選導覽列上的「SUBMIT」，確定 problem 是我們要解決的，選擇我們的程式的 language，接著貼上 source code 並按下「Submit」按鈕。

            按下按鈕後，會跳到 Status 這一頁，若我們的答案成功在題目的要求下解決此問題，在「Verdict」這一欄會出現綠色的 「Accepted」。

            如果我們在第 # 個測試中輸出的答案與測試器期望的答案不同，會出現「Wrong answer on test #」, 若是 source code 編譯錯誤，會出現「Compilation error」。若在第 # 次的測試中超過記憶體大小限制，會出現「Memory limit exceeded on test #」。若在第 # 次的測試中超過時限制，會出現「Time limit exceeded on test #」。此時我們可以按下左邊的流水號，以檢視出現錯誤的測項、錯誤訊息等。

        3. 參考其他人的答案

            寫完一道題目後，最重要的是檢討自己的答案。檢討的方法有很多，其中之一是觀察別人的解法。由導覽列 → PROBLEMSET 中找出我們的題目，並按下右方解題人數，即可看到大家對此題所寫的解法。

            [![](http://4.bp.blogspot.com/-tnc7IUZhb1Y/ULNpNbdg2AI/AAAAAAAAADs/dclmNcnjMWE/s1600/solved.png)](http://4.bp.blogspot.com/-tnc7IUZhb1Y/ULNpNbdg2AI/AAAAAAAAADs/dclmNcnjMWE/s1600/solved.png)

            在頁面最下方可以自訂排序規則，我們可以依照 Solution Size (source code 大小) 或 Execution Time (執行時間長短) 來排序，以方便我們找出想要參考的答案。右方可以選擇我們想要看到的語言。

            [![](http://1.bp.blogspot.com/-0UMrCC6I4wE/ULNqulcBplI/AAAAAAAAAD0/uIQyrdnF9gE/s1600/solved_lang.png)](http://1.bp.blogspot.com/-0UMrCC6I4wE/ULNqulcBplI/AAAAAAAAAD0/uIQyrdnF9gE/s1600/solved_lang.png)

            讀者可參考此題的 [Python 版解法](http://codeforces.com/contest/1/submission/1647521)、[Ruby 版解法](http://codeforces.com/contest/1/submission/2337277)、[PHP 版解法](http://codeforces.com/contest/1/submission/889578)、[C 版解法](http://codeforces.com/contest/1/submission/1337822)、[C++ 版解法](http://codeforces.com/contest/1/submission/759)、[C# 版解法](http://codeforces.com/contest/1/submission/2032793)、[Java 版解法](http://codeforces.com/contest/1/submission/604386)、[Scala 版解法](http://codeforces.com/contest/1/submission/1903268)。
