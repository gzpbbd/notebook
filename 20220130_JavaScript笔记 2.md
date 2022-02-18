# JavaScript 进阶

## 事件

```html
<some-HTML-element some-event='JavaScript 代码'> 单引号
<some-HTML-element some-event="JavaScript 代码"> 双引号
    
<button onclick="getElementById('demo').innerHTML=Date()">现在的时间是?</button>
```

常见的HTML事件的列表:

| 事件        | 描述                                 |
| :---------- | :----------------------------------- |
| onchange    | HTML 元素改变                        |
| onclick     | 用户点击 HTML 元素                   |
| onmouseover | 鼠标指针移动到指定的元素上时发生     |
| onmouseout  | 用户从一个 HTML 元素上移开鼠标时发生 |
| onkeydown   | 用户按下键盘按键                     |
| onload      | 浏览器已完成页面的加载               |

## JSON

参考教程：https://www.runoob.com/js/js-json.html

| 函数                                                         | 描述                                           |
| :----------------------------------------------------------- | :--------------------------------------------- |
| [JSON.parse()](https://www.runoob.com/js/javascript-json-parse.html) | 用于将一个 JSON 字符串转换为 JavaScript 对象。 |
| [JSON.stringify()](https://www.runoob.com/js/javascript-json-stringify.html) | 用于将 JavaScript 值转换为 JSON 字符串。       |

### [JSON.parse()](https://www.runoob.com/js/javascript-json-parse.html)

#### 语法

```
JSON.parse(text[, reviver])
```

#### 参数说明

- **text:**必需， 一个有效的 JSON 字符串。
- **reviver:** 可选，一个转换结果的函数， 将为对象的每个成员调用此函数。

#### 返回值

返回给定 JSON 字符串转换后的对象。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<h2>从 JSON 字符串中创建一个对象</h2>
<p id="demo"></p>
<script>
var text = '{"employees":[' +
	'{"name":"菜鸟教程","site":"http://www.runoob.com" },' +
	'{"name":"Google","site":"http://www.Google.com" },' +
	'{"name":"Taobao","site":"http://www.taobao.com" }]}';
obj = JSON.parse(text);
document.getElementById("demo").innerHTML =
	obj.employees[1].name + " " + obj.employees[1].site;
</script>

</body>
</html>
```

### JSON.stringify()

#### 语法

```
JSON.stringify(value[, replacer[, space]])
```

#### 参数说明

- value:

  必需， 要转换的 JavaScript 值（通常为对象或数组）。

- replacer:

  可选。用于转换结果的函数或数组。

  如果 replacer 为函数，则 JSON.stringify 将调用该函数，并传入每个成员的键和值。使用返回值而不是原始值。如果此函数返回 undefined，则排除成员。根对象的键是一个空字符串：""。

  如果 replacer 是一个数组，则仅转换该数组中具有键值的成员。成员的转换顺序与键在数组中的顺序一样。

- space:

  可选，文本添加缩进、空格和换行符，如果 space 是一个数字，则返回值文本在每个级别缩进指定数目的空格，如果 space 大于 10，则文本缩进 10 个空格。space 也可以使用非数字，如：\t。

#### 返回值

返回包含 JSON 文本的字符串。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<p id="demo"></p>
<script>
var str = {"name":"菜鸟教程", "site":"http://www.runoob.com"}
str_pretty1 = JSON.stringify(str)
document.write( "只有一个参数情况：" );
document.write( "<br>" );
document.write("<pre>" + str_pretty1 + "</pre>" );
document.write( "<br>" );
str_pretty2 = JSON.stringify(str, null, 4) //使用四个空格缩进
document.write( "使用参数情况：" );
document.write( "<br>" );
document.write("<pre>" + str_pretty2 + "</pre>" ); // pre 用于格式化输出
</script>

</body>
</html>
```

## javascript:void(0) 含义

void: 该操作符指定要计算一个表达式但是不返回值

语法格式如下：

```javascript
void func()
javascript:void func()
// 或者
void(func())
javascript:void(func())
```

实例：

```html
下面的代码创建了一个超级链接，当用户点击以后不会发生任何事:
<a href="javascript:void(0)">单击此处什么也不会发生</a>
以下实例中，在用户点击链接后显示警告信息：
<a href="javascript:void(alert('Warning!!!'))">点我!</a>
```

#### href="#"与href="javascript:void(0)"的区别

“#” 包含了一个位置信息，默认的锚是#top 也就是网页的上端。而javascript:void(0), 仅仅表示一个死链接。
在页面很长的时候会使用 # 来定位页面的具体位置，格式为：# + id。

```html
<a href="javascript:void(0);">点我没有反应的!</a>
<a href="#pos">点我定位到指定位置!</a>
<br>
...
<br>
<p id="pos">尾部定位点</p>
```

## 异步编程 

### Ajax 与 JQuery

javaScript是用于Web客户端开发的脚本语言，Ajax是基于JS语言，主要组合JS、CSS、XML三种技术的新技术，是用于创建交互式网页应用的网页开发技术。 jQuery是JS的框架，基于JS语言，集合Ajax技术开发出来的JS库，封装JS和Ajax的功能，提供函数接口，大大简化了Ajax，JS的操作。

### setTimeout()

在设定的时间达到后，调用回调函数

```javascript
// 实例 1
function print() {
    document.getElementById("demo").innerHTML="RUNOOB!";
}
setTimeout(print, 3000);
// 或者
setTimeout(function () {
    document.getElementById("demo").innerHTML="RUNOOB!";
}, 3000);

// 实例 2
setTimeout(function () {
    document.getElementById("demo1").innerHTML="RUNOOB-1!";
}, 3000);
document.getElementById("demo2").innerHTML="RUNOOB-2!";
console.log("2");
```

### Ajax

此处是 javascript 原生 ajax API。（axios 是一个流行的 ajax 第三方库）

有关于 AJAX 详细请参见：https://www.runoob.com/ajax/ajax-tutorial.html

- AJAX = Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。
- AJAX 最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。
- AJAX 不需要任何浏览器插件，但需要用户允许JavaScript在浏览器上执行。
- **AJAX 编程的核心是操作 XMLHttpRequest 对象** 

#### 简单例子

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
function loadXMLDoc()
{
	var xmlhttp=new XMLHttpRequest(); // 1. 创建对象
	xmlhttp.onreadystatechange=function()  // 2. 设置回调函数
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200) // 4：请求已完成，200：成功获取数据
		{
			document.getElementById("myDiv").innerHTML=xmlhttp.responseText; // 使用响应的数据
		}
	}
	xmlhttp.open("GET","/try/ajax/ajax_info.txt",true); // 3. 设置请求的 method 与 url
	xmlhttp.send(); // 4. 发送请求
}
</script>
</head>
<body>

<div id="myDiv"><h2>使用 AJAX 修改该文本内容</h2></div>
<button type="button" onclick="loadXMLDoc()">修改内容</button>

</body>
</html>
```

#### 创建对象与发送请求

```javascript
// 创建
let xmlhttp = new XMLHttpRequest();

// 发送 GET 请求
  // example 1
xmlhttp.open("GET","/try/ajax/demo_get.php",true); // 可能得到缓存的结果
  // example 2
xmlhttp.open("GET","/try/ajax/demo_get.php?t=" + Math.random(),true); // 添加唯一的 ID从而避免使用缓存
  // example 3
xmlhttp.open("GET","/try/ajax/demo_get2.php?fname=Henry&lname=Ford",true); // 添加信息
xmlhttp.send();

// 发送 POST 请求
  // example 1
xmlhttp.open("POST","/try/ajax/demo_post.php",true);
xmlhttp.send();
  // example 2
xmlhttp.open("POST","/try/ajax/demo_post2.php",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded"); // 设置请求头
xmlhttp.send("fname=Henry&lname=Ford"); // 添加信息

```

| 方法                             | 描述                                                         |
| :------------------------------- | :----------------------------------------------------------- |
| open(*method*,*url*,*async*)     | 规定请求的类型、URL 以及是否异步处理请求。***method***：请求的类型；GET 或 POST  ***url***：文件在服务器上的位置  ***async***：true（异步）或 false（同步） |
| send(*string*)                   | 将请求发送到服务器。***string***：仅用于 POST 请求           |
| setRequestHeader(*header,value*) | 向请求添加 HTTP 头。*header*: 规定头的名称*value*: 规定头的值 |

- 当使用 async=true 时，请规定在响应处于 onreadystatechange 事件中的就绪状态时执行的函数：

- 如需使用 async=false，请将 open() 方法中的第三个参数改为 false （当您使用 async=false 时，请不要编写 onreadystatechange 函数 - 把代码放到 send() 语句后面即可）

  ```javascript
  xmlhttp.open("GET","/try/ajax/ajax_info.txt",false);
  xmlhttp.send();
  document.getElementById("myDiv").innerHTML = xmlhttp.responseText; // 不需要回调函数，直接使用数据
  ```

  

与 POST 相比，GET 更简单也更快，并且在大部分情况下都能用。

然而，在以下情况中，请使用 POST 请求：

- 不愿使用缓存文件（更新服务器上的文件或数据库）
- 向服务器发送大量数据（POST 没有数据量限制）
- 发送包含未知字符的用户输入时，POST 比 GET 更稳定也更可靠

#### 获取响应的数据

如需获得来自服务器的响应，请使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。

| 属性         | 描述                                                      |
| :----------- | :-------------------------------------------------------- |
| responseText | 获得字符串形式的响应数据。                                |
| responseXML  | 获得 XML 形式的响应数据。                                 |
| response     | 根据 xhr.responseType 的不同，xhr.response 为不同数据类型 |

```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
function loadXMLDoc()
{
	var xmlhttp = new XMLHttpRequest();	
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById("myDiv").innerHTML=xmlhttp.responseText; // 获取 text
		}
	}
	xmlhttp.open("GET","/try/ajax/ajax_info.txt",true);
	xmlhttp.send();
}
</script>
</head>
<body>

<div id="myDiv"><h2>使用 AJAX 修改该文本内容</h2></div>
<button type="button" onclick="loadXMLDoc()">修改内容</button>

</body>
</html>
```

#### XMLHttpRequest 对象的属性

| 属性               | 描述                                                         |
| :----------------- | :----------------------------------------------------------- |
| onreadystatechange | 存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数。 |
| readyState         | 存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。**0**: 请求未初始化  **1**: 服务器连接已建立   **2**: 请求已接收  **3**: 请求处理中  **4**: 请求已完成，且响应已就绪 |
| status             | 200: "OK" 404: 未找到页面                                    |
| responseType       | 返回体类型，如果设置为 xhr.responseType='json'，则 xhr.response 直接为 json 对象 |
| timeout            | 超时时间，以毫秒为单位                                       |
| ontimeout          | 超时后的回调函数                                             |
| onerror            | 其它异常（如网络中断）的回调函数                             |
| abort()            | 取消请求                                                     |
|                    |                                                              |

#### 解决缓存的问题

在 url 末尾加上 "?t="+Date.now()
