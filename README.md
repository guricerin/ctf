# ctf

## Env

- Windows 11
- WSL2 Ubuntu 20.04

## Tool

### Forensics

デジタルデータの解析。  

#### [binwalk](https://github.com/ReFirmLabs/binwalk)

- ファイル中に埋め込まれている別のファイルを解析。  

```bash
$ sudo apt install binwalk
$ binwalk <File>
```

#### [foremost](http://foremost.sourceforge.net/)

- 内部データ構造に基づいてファイルを復元する。
- ディスクイメージファイルにも適用可能。

```bash
$ sudo apt install foremost
$ foremost <File>
```

#### [exiftool](https://exiftool.org/)

- 画像や動画などのメディアファイルからExif情報を抽出。

```bash
$ sudo apt install exiftool
$ exiftool <Media-File>
```

#### [The Sleuth Kit](https://www.sleuthkit.org/index.php)

##### fls

- ディスクイメージファイルを解析。

```bash
$ fls <Disk-image-File>
```

##### icat

- ディスクイメージファイルを復元。

```bash
$ icat <Disk-image-File> <inode-Number> > <output-File>
```

##### mmls

- ボリュームシステム(パーティションテーブル)のパーティションレイアウト情報を表示。

```bash
$ mmls <Disk-image-File>
```

#### [pdftotext](https://poppler.freedesktop.org/)

- pdf中のテキストデータを抽出。

```bash
$ sudo apt install poppler-utils
$ pdftotext <PDF-File>
```
