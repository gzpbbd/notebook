# 版本

| 年份 | 名称           | 描述                                              |
| :--- | :------------- | :------------------------------------------------ |
| 1997 | ECMAScript 1   | 第一个版本                                        |
| 1998 | ECMAScript 2   | 版本变更                                          |
| 1999 | ECMAScript 3   | 添加正则表达式 添加 try/catch                     |
|      | ECMAScript 4   | 没有发布                                          |
| 2009 | ECMAScript 5   | 添加 "strict mode"，严格模式 添加 JSON 支持       |
| 2011 | ECMAScript 5.1 | 版本变更                                          |
| 2015 | ECMAScript 6   | 添加类和模块                                      |
| 2016 | ECMAScript 7   | 增加指数运算符 (**) 增加 Array.prototype.includes |

# JavaScript包含的内容

- ECMAScript：由 ECMA-262 定义并提供核心功能。
- 文档对象模型（DOM）：提供与网页内容交互的方法和接口。
- 浏览器对象模型（BOM）：提供与浏览器交互的方法和接口。

# 基础部分

## 脚本语言

JavaScript 是脚本语言，浏览器会在读取代码时，逐行地执行脚本代码。而对于传统编程来说，会在执行前对所有代码进行编译

## 输出

JavaScript 没有任何打印或者输出的函数。

- 使用 console.log() 写入到浏览器的控制台。

- 使用 window.alert() 弹出警告框。

- 使用 document.write() 方法将内容写到 HTML 文档中。

- 使用 innerHTML 写入到 HTML 元素。

  ```javascript
  document.getElementById("demo").innerHTML = "段落已修改。";
  ```

## 语法

### 数据类型

在 JavaScript 中有 **6 种不同的基本数据类型**：

- string
- number
- boolean
- object
- function
- symbol

**3 种对象类型**：

- Object
- Date
- Array

**2 个不包含任何值的数据类型**：

- null
- undefined

```javascript
// 语句末尾的分号可有可无，省略分号意味着由解析器确定语句在哪里结尾
// 数字
3.14
1001
123e5
// 布尔
var x=true;
var y=false;
// 字符串
var carname="Volvo XC60";
var carname='Volvo XC60';
// undefined 这个值表示变量不含有值。
// 可以通过将变量的值设置为 null 来清空变量。
cars=null;

// 数组（Array）
var cars=["Saab","Volvo","BMW"];
var cars=new Array("Saab","Volvo","BMW");
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";

var message; // 变量的值 undefined

// ECMAScript 有 6 种简单数据类型（也称为原始类型）：Undefined、Null、Boolean、Number、 String 和 Symbol。Symbol（符号）是 ECMAScript 6 新增的
var length = 16;                                  // Number 通过数字字面量赋值
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值
```

#### 字符串 String

```javascript
var carname = "Volvo XC60";
var carname = 'Volvo XC60';

var answer = "He is called 'Johnny'";
var answer = 'He is called "Johnny"';

var x = 'It\'s alright';
var y = "He is called \"Johnny\"";

var character = carname[7];

var sln = carname.length;

var x = "John";
var y = new String("John"); // 不要创建 String 对象。它会拖慢执行速度，并可能产生其他副作用
typeof x // 返回 String
typeof y // 返回 Object

var x = "John";             
var y = new String("John");
(x === y) // 结果为 false，因为 x 是字符串，y 是对象 // === 为绝对相等，即数据类型与值都必须相等。
```

##### 字符串属性

| 属性        | 描述                       |
| :---------- | :------------------------- |
| constructor | 返回创建字符串属性的函数   |
| length      | 返回字符串的长度           |
| prototype   | 允许您向对象添加属性和方法 |

##### 字符串方法

| 方法                | 描述                                                         |
| :------------------ | :----------------------------------------------------------- |
| charAt()            | 返回指定索引位置的字符                                       |
| charCodeAt()        | 返回指定索引位置字符的 Unicode 值                            |
| concat()            | 连接两个或多个字符串，返回连接后的字符串                     |
| fromCharCode()      | 将 Unicode 转换为字符串                                      |
| indexOf()           | 返回字符串中检索指定字符第一次出现的位置                     |
| lastIndexOf()       | 返回字符串中检索指定字符最后一次出现的位置                   |
| localeCompare()     | 用本地特定的顺序来比较两个字符串                             |
| match()             | 找到一个或多个正则表达式的匹配                               |
| replace()           | 替换与正则表达式匹配的子串                                   |
| search()            | 检索与正则表达式相匹配的值                                   |
| slice()             | 提取字符串的片断，并在新的字符串中返回被提取的部分           |
| split()             | 把字符串分割为子字符串数组                                   |
| substr()            | 从起始索引号提取字符串中指定数目的字符                       |
| substring()         | 提取字符串中两个指定的索引号之间的字符                       |
| toLocaleLowerCase() | 根据主机的语言环境把字符串转换为小写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| toLocaleUpperCase() | 根据主机的语言环境把字符串转换为大写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| toLowerCase()       | 把字符串转换为小写                                           |
| toString()          | 返回字符串对象值                                             |
| toUpperCase()       | 把字符串转换为大写                                           |
| trim()              | 移除字符串首尾空白                                           |
| valueOf()           | 返回某个字符串对象的原始值                                   |

##### 字符串的加法

任意数据类型与字符串相加，都会变为字符串

#### Number

```javascript
(123).toString() // 123
(100 + 23).toString() // 123
```

| 方法            | 描述                                                 |
| :-------------- | :--------------------------------------------------- |
| toExponential() | 把对象的值转换为指数计数法。                         |
| toFixed()       | 把数字转换为字符串，结果的小数点后有指定位数的数字。 |
| toPrecision()   | 把数字格式化为指定的长度。                           |

#### null

- null是一个只有一个值的特殊类型。表示一个空对象引用
- 用 typeof 检测 null 返回是object。
- 可以设置为 null 来清空对象

#### undefined

- undefined 是一个没有设置值的变量
- typeof 一个没有值的变量会返回 undefined。
- 任何变量都可以通过设置值为 undefined 来清空。 类型为 undefined.

#### undefined 和 null 的区别

null 和 undefined 的值相等，但类型不等:

```javascript
typeof undefined             // undefined
typeof null                  // object
null === undefined           // false
null == undefined            // true
```



### 变量

变量 是松散类型的，意思是变量可以用于保存任何类型的数据
声明变量：var、const 和 let。
其中，var 在 ECMAScript 的所有版本中都可以使用，而 const 和 let 只能在 ECMAScript 6 及更晚的版本中使用

编程规范: 不使用 var， const 优先，let 次之

#### var

- var 声明作用域： 使用 var 操作符定义的变量会成为包含它的函数的局部变量
- 在函数内定义变量时省 略 var 操作符，可以创建一个全局变量
- var 声明提升：使用这个关键字声明的变量会自动提升到函数作用域顶部
- 反复多次 使用 var 声明同一个变量也没有问题

#### let

- let 跟 var 的作用差不多，但有着非常重要的区别。最明显的区别是，let 声明的范围是块作用域， 而 var 声明的范围是函数作用域
- let 也不允许同一个块作用域中出现冗余声明
- let 与 var 的另一个重要的区别，就是 let 声明的变量不会在作用域中被提升。
- 与 var 关键字不同，使用 let 在全局作用域中声明的变量不会成为 window 对象的属性（var 声明的变量则会）
- 在 let 出现之前，for 循环定义的var变量会渗透到循环体外部，而 let 不会

#### const

- const 的行为与 let 基本相同，唯一一个重要的区别是用它声明变量时必须同时初始化变量，且尝试修改 const 声明的变量会导致运行时错误。
- const 声明的限制只适用于它指向的变量的引用。换句话说，如果 const 变量引用的是一个对象， 那么修改这个对象内部的属性并不违反 const 的限制。

#### 声明变量类型

当声明新变量时，可以使用关键词 "new" 来声明其类型：

```javascript
// JavaScript 变量均为对象。当您声明一个变量时，就创建了一个新的对象。???
var carname=new String;
var x=      new Number;
var y=      new Boolean;
var cars=   new Array;
var person= new Object;
```

### 

|      |      |
| :--- | :--- |
|      |      |
|      |      |

### 对象

```javascript
// 对象（Object）, JavaScript 对象是键值对的容器, JavaScript 对象是属性和方法的容器。
var person={firstname:"John", lastname:"Doe", id:5566};
var person = {
    firstName: "John",
    lastName : "Doe",
    id : 5566,
    fullName : function() 
	{
       return this.firstName + " " + this.lastName;
    }
};

// 对象属性有两种寻址方式：
var name=person.lastname;
var name=person["lastname"];
```



### 函数

```javascript
function functionname()
{
    // 执行代码
}

function myFunction(var1,var2)
{
// 代码
}

function myFunction()
{
    var x=5;
    return x;
}

function myFunction(a,b)
{
    if (a>b)
    {
        return; // 返回值是可选的
    }
    x=a+b
}
```



### 比较运算符

| 运算符 | 描述                                               |
| :----- | :------------------------------------------------- |
| ===    | 绝对等于（值和类型均相等）                         |
| !==    | 不绝对等于（值和类型有一个不相等，或两个都不相等） |

### For 循环 与 For/In 循环

```javascript
for (语句 1; 语句 2; 语句 3)
{
    被执行的代码块
}

// for/in 语句循环遍历对象的属性
var person={fname:"Bill",lname:"Gates",age:56};  
for (x in person)  // x 为属性名：fname, lname, age
{
    console.log(x)
}
```

### typeof 操作符

```javascript
typeof "John"                 // 返回 string
typeof 3.14                   // 返回 number
typeof NaN                    // 返回 number
typeof false                  // 返回 boolean
typeof [1,2,3,4]              // 返回 object
typeof {name:'John', age:34}  // 返回 object
typeof new Date()             // 返回 object
typeof function () {}         // 返回 function
typeof myCar                  // 返回 undefined (如果 myCar 没有声明)
typeof null                   // 返回 object
```

### 类型转换

Number() 转换为数字， String() 转换为字符串， Boolean() 转换为布尔值。

| 原始值              | 转换为数字 | 转换为字符串      | 转换为布尔值 | 实例                                                         |
| :------------------ | :--------- | :---------------- | :----------- | :----------------------------------------------------------- |
| false               | 0          | "false"           | false        | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_false) |
| true                | 1          | "true"            | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_true) |
| 0                   | 0          | "0"               | false        | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_number_0) |
| 1                   | 1          | "1"               | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_number_1) |
| "0"                 | 0          | "0"               | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_string_0) |
| "000"               | 0          | "000"             | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_string_000) |
| "1"                 | 1          | "1"               | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_string_1) |
| NaN                 | NaN        | "NaN"             | false        | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_nan) |
| Infinity            | Infinity   | "Infinity"        | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_infinity) |
| -Infinity           | -Infinity  | "-Infinity"       | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_infinity_minus) |
| ""                  | 0          | ""                | false        | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_string_empty) |
| "20"                | 20         | "20"              | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_string_number) |
| "Runoob"            | NaN        | "Runoob"          | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_string_text) |
| [ ]                 | 0          | ""                | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_array_empty) |
| [20]                | 20         | "20"              | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_array_one_number) |
| [10,20]             | NaN        | "10,20"           | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_array_two_numbers) |
| ["Runoob"]          | NaN        | "Runoob"          | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_array_one_string) |
| ["Runoob","Google"] | NaN        | "Runoob,Google"   | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_array_two_strings) |
| function(){}        | NaN        | "function(){}"    | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_function) |
| { }                 | NaN        | "[object Object]" | true         | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_object) |
| null                | 0          | "null"            | false        | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_null) |
| undefined           | NaN        | "undefined"       | false        | [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_type_convert_undefined) |

### 自动转换类型

当 JavaScript 尝试操作一个 "错误" 的数据类型时，会自动转换为 "正确" 的数据类型。

```javascript
5 + null    // 返回 5         null 转换为 0
"5" + null  // 返回"5null"   null 转换为 "null"
"5" + 1     // 返回 "51"      1 转换为 "1" 
"5" - 1     // 返回 4         "5" 转换为 5
```



## this 关键字

在 JavaScript 中 this 不是固定不变的，它会随着执行环境的改变而改变。

- 在**方法**中，this 表示该方法所属的对象。
- 在**事件**中，this 表示接收事件的元素。
- 如果单独使用，this 表示全局对象。（在浏览器中，window 就是该全局对象为 [**object Window**]）
- 在函数中，this 表示全局对象。
- 在函数中，在严格模式下，this 是未定义的(undefined)。
- 类似 call() 和 apply() 方法可以将 this 引用到任何对象。

## 显式函数绑定

在 JavaScript 中函数也是对象，对象则有方法，apply 和 call 就是函数对象的方法。这两个方法异常强大，他们允许切换函数执行的上下文环境（context），即 this 绑定的对象。

在下面实例中，当我们使用 person2 作为参数来调用 person1.fullName 方法时, **this** 将指向 person2, 即便它是 person1 的方法：

```javascript
var person1 = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}
var person2 = {
  firstName:"John",
  lastName: "Doe",
}
person1.fullName.call(person2);  // 返回 "John Doe"
```



