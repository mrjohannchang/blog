title: Using Express to Handle File Uploading
date: 2015-10-12 12:42:20
tags:
- programming
coverImage: expressjs.jpg
coverMeta: out
---

[Express](https://github.com/strongloop/express) 本身不管上傳，要透過 [Multer](https://github.com/expressjs/multer) 來處理。

Multer 手冊特別註明：
<!-- more -->
> **NOTE**: Multer will not process any form which is not multipart (multipart/form-data).

意思就是說 `Content-Type` 必須要是 `multipart/form-data`。

以 Python 的 [Requests](http://docs.python-requests.org/) 當 client 為例：
```py
response = requests.post('http://httpbin.org/post', files={'example_file': ('example.zip', open('a_example.zip', 'rb'))})
```

Request 這樣用 `Content-Type` 預設就是 `multipart/form-data`
http://httpbin.org/post 是測試的好幫手，可以

```py
pprint.pprint(response.json()['headers'])
```

把 server 收到的 header dump 出來。
http://stackoverflow.com/questions/12385179/how-to-send-a-multipart-form-data-with-requests-in-python

其中 example_file 對應 Multer 的：

```js
upload.single('example_file')
```

如果沒有對起來，會出現對 trace 沒有幫助的 error：

```txt
Error: Unexpected field
    at makeError (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/lib/make-error.js:12:13)
    at wrappedFileFilter (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/index.js:39:19)
    at Busboy.<anonymous> (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/lib/make-middleware.js:112:7)
    at emitMany (events.js:108:13)
    at Busboy.emit (events.js:182:7)
    at Busboy.emit (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/node_modules/busboy/lib/main.js:31:35)
    at PartStream.<anonymous> (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/node_modules/busboy/lib/types/multipart.js:209:13)
    at emitOne (events.js:77:13)
    at PartStream.emit (events.js:169:7)
    at HeaderParser.<anonymous> (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/node_modules/busboy/node_modules/dicer/lib/Dicer.js:51:16)
    at emitOne (events.js:77:13)
    at HeaderParser.emit (events.js:169:7)
    at HeaderParser._finish (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/node_modules/busboy/node_modules/dicer/lib/HeaderParser.js:70:8)
    at SBMH.<anonymous> (/home/changyuheng/production/ultima-cloud-server/node_modules/multer/node_modules/busboy/node_modules/dicer/lib/HeaderParser.js:42:12)
    at emitMany (events.js:108:13)
    at SBMH.emit (events.js:182:7)
```
