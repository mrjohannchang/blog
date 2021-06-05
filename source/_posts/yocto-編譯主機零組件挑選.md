---
title: Yocto 編譯主機零組件挑選
date: 2021-06-06
categories:
- Hardware
---

# 背景

需求：程式編譯，主要編譯 Yocto
預算：4.5 萬

# 零件挑選

## 中央處理器（CPU）

挑選 CPU 有幾個重點，依優先順序分別為：售價（預算）、效能、功耗（耗電量、廢熱量）、C/P 值。

OpenBenchmarking 上搜集了各型號 CPU 的 [Linux Kernel 編譯時間](https://openbenchmarking.org/test/pts/build-linux-kernel)，可用以評估各型 CPU 多核心編譯的效能：

![Timed-Linux-Kernel-Compilation.png](Timed-Linux-Kernel-Compilation.png)

伺服器版的 CPU 太貴，直接跳過。[AMD Ryzen™ 9 5950X](https://www.amd.com/en/products/cpu/amd-ryzen-9-5950x)、[AMD Ryzen™ 9 3950X](https://www.amd.com/en/products/cpu/amd-ryzen-9-3950x) 及 [Intel® Core™ i9-10980XE](https://ark.intel.com/content/www/us/en/ark/products/198017/intel-core-i9-10980xe-extreme-edition-processor-24-75m-cache-3-00-ghz.html) 這三顆 CPU 是目前家用主機的頂規。

Intel 這顆效能表現與 AMD 這二顆相伯仲，但功耗高很多，差不多是風冷散熱的極限，所以先剔除。再來因為 5950X 和 3950X 這二顆都缺貨，也只能放棄。繼續往下的選擇中，[AMD Ryzen™ 9 5900X](https://www.amd.com/en/products/cpu/amd-ryzen-9-5900x) 效能相差不大，有貨，且 C/P 值比 5950X、3950X 都高很多，因此沒有什麼懸念，就選它了。

## 主機板

相容 AMD Ryzen™ 9 5900X AM4 規格且有現貨的晶片組有 B450、X470、[A520](https://www.amd.com/en/chipsets/a520)、[B550](https://www.amd.com/en/chipsets/b550) 和 [X570](https://www.amd.com/en/chipsets/x570)。符合目前需求的最便宜選擇是 B450，但可惜目前 Mini-ITX 的版本缺貨，只能往更高階看。因為想保留未來插高階顯示卡和 PCIe 4.0 SSD 的空間，所以從在 B550 和 X570 之間選了比較便宜的 B550。

![AM4-Chipset-Spec.png](AM4-Chipset-Spec.png)

![AM4-Chipset-Compatibility.png](AM4-Chipset-Compatibility.png)

## 記憶體

依照經驗，一般軟體專案編譯所需的記憶體大小，約略是 CPU 執行緒數多少條，記憶體就要多少 GB。除此之外，我也先在舊的電腦上，參考這個[網頁](https://www.linuxatemyram.com/)，分別在掛上 Swap 和卸載 Swap 的情形下做實際編譯，並比較記憶體的使用狀況。

測試機器：

- Intel® Core™ i7-8700K (6 核、12 緒)

```
$ lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              12
On-line CPU(s) list: 0-11
Thread(s) per core:  2
Core(s) per socket:  6
Socket(s):           1
...
```

- 記憶體 16 GB

```
$ free
              total        used        free      shared  buff/cache   available
Mem:       16303912     1840356    13280940      873236     1182616    13286976
Swap:       2097148           0     2097148
```

1.  有掛載 Swap：
    掛 Swap：
    
    ```
    swapon -a
    ```
    
    清記憶體：
    
    ```
    sync; echo 3 > /proc/sys/vm/drop_caches
    ```
    
    開始搜集記憶體使用狀況：
    
    ```
    free -s 1 | tee memory-usage-log-swapon.txt
    ```
    
    進行編譯。
    編譯後確認，編譯過程中最低可用記憶體剩餘量：
    
    ```
    cat memory-usage-log-swapon.txt | grep Mem | awk '{print $7}' | sort -n | head -n 1
    ```
    
    及最高 Swap 使用量：
    
    ```
    cat memory-usage-log-swapon.txt | grep Swap | awk '{print $3}' | sort -nr | head -n 1
    ```
    
    最低可用記憶體剩餘量為 5.46 GB，最高 Swap 使用量為 321.75 MB。因此在 12 緒的 CPU 下做編譯，16 GB 的記憶體是足夠使用的。
    
2.  無掛載 Swap：
    卸 Swap：
    
    ```
    swapoff -a
    ```
    
    清記憶體：
    
    ```
    sync; echo 3 > /proc/sys/vm/drop_caches
    ```
    
    開始搜集記憶體使用狀況：
    
    ```
    free -s 1 | tee memory-usage-log-swapoff.txt
    ```
    
    進行編譯。
    編譯後確認，編譯過程中最低可用記憶體剩餘量：
    
    ```
    cat memory-usage-log-swapoff.txt | grep Mem | awk '{print $7}' | sort -n | head -n 1
    ```
    
    最低可用記憶體剩餘量為 5.24 GB，與編譯中 1 條執行緒約需要使用 1 GB 的經驗相符。

AMD Ryzen™ 9 5900X AM4 是 12 核 24 緒，因此 32 GB 的記憶體應足夠使用。同樣大小的記憶體也有價差，時脈、CL 值、會不會發光、品牌等都有影響。我買了 DDR4-3600 CL18，其實應該選 DDR4-3200 CL16 的就好，因為二者效能差不多，但 DDR4-3600 CL18 的價格高了近 20%。這邊預算沒有控制好。

## 固態硬碟

儲存空間大一點比較方便，目前能買到的最大大小為 2 TB，[WD_BLACK™ SN750](https://shop.westerndigital.com/products/internal-drives/wd-black-sn750-nvme-ssd#WDS250G3X0C) 太貴，就挑了使用國產控制器（群聯）一樣五年保的 [Pioneer APS-SE20Q](https://pioneer-iot.com/product/internal-ssd/internal-ssdaps-se20q/)。

## 顯示卡

基本上除了安裝以外都不會接螢幕，因此低階的即可。但仍希望起碼能推動 4K 的螢幕，所以挑了 [GeForce GT 1030](https://www.nvidia.com/en-us/geforce/graphics-cards/gt-1030/specifications/)。

## 機殼

因為想要小機殼，所以鎖定 Mini-ITX 的機殼。小機殼內部比較擁擠，裝高度發熱的元件要特別注意通風、散熱。參考了一些在 YouTube 上看到的機殼：

![Cases.png](Cases.png)

發現符合我期待的散熱方式及電源位置的只有 [NZXT H210](https://nzxt.com/product/h210)，所以就選了它。

![Airflow-in-Cases.png](Airflow-in-Cases.png)

挑選小型的機殼時，除了要注意 CPU 散熱器的高度外，還要看散熱器的體積對機殼內通風的影響。H210 的內部配置有一些亮點：

1.  前進氣風扇的尺寸比後出風風扇的大，因此很容易可以達到機殼內正壓的配置。
2.  風流設計看起來很合理，前方進風後方出風，中間會吹到 CPU、顯示卡和電源。
3.  有附防塵濾網。
4.  電源下置且有獨立空間。
5.  可使用 ATX 的電源。
6.  電源直接貼在背板，電源線可以直接接到電源上，不需要透過機殼內的電源延長線。

像這種小型的機殼，因為顯卡離機殼底部很近，因此還要注意，若機殼下方會裝風扇，其風向應與顯卡風扇的風向一致。不是所有顯卡的風扇都是往晶片方向吹的，也有反著吹的：

![Display-Card-Wind-Direction.png](Display-Card-Wind-Direction.png)

補充說明，我會避免選擇將電源供應器定位為主要排風元件的機殼（如後上置型的）。因為電源供應器很怕熱，長期在較熱環境工作的電源供應器，除了壽命比較短之外，也很危險（可參見全漢[官網說明](https://www.fsp-group.com/tw/knowledge-prd-4.html)）。所以如果機殼內有獨立空間可放置電源供應器是最理想的，這樣電源供應器就不會與 CPU、顯示卡等高發熱元件混在同一空間內。

## CPU 散熱器

散熱器實在太多了，所以我直接在以安靜著稱的貓頭鷹裡挑。因為希望能與機殼設計的水平風流相配合，所以只看塔式散熱器。5900X 蠻熱的，所以需要散熱能力好一點的，同時我又不喜歡記憶體上方被風扇擋住，所以挑了 [Noctua NH-D15S](https://www.google.com/search?client=firefox-b-d&q=NH-D15s)。

## 電源供應器

電源供應器是耗材，它的供應瓦數是會衰減的。預算許可的話，就把瓦數買到 CPU + 顯卡功耗的 2 倍，這樣電源供應器在其他零件壞掉前應該都會是好的。愛護地球，在能負擔的範圍內選轉換功率高一點的。
