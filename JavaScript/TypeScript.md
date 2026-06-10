# TypeScript

## 原始数据类型

### 布尔Boolean

使用**boolean**定义布尔值类型

```typescript
let isDone:boolean=false
```

使用构造函数**Boolean**创造的对象不是布尔值，而是一个**Boolean**对象

```typescript
let createByNewBoolean:Boolean=new Boolean(1)
```

也可以直接调用**Boolean**返回一个**boolean**类型

```typescript
let createByNewBoolean:boolean=Boolean(1)
```

在**TypeScript**中**boolean**是**JavaScript**中的基本类型，而**Boolean**是**JavaScript**中的构造函数

其他类型除了(**null**和**undefined**)都是一样的，不再赘述

***

### 数值number

使用**number**定义数值类型

```typescript
let decNumber:number=6
let hexNumber:number=0xf00d //十六进制
let binaryNumber:number=0b1010 //二进制
let octalNumber:number=0o744 //八进制
let notNumber:number=NaN
let infinityNumber:number=Infinity
```

***

### 字符串string

使用**string**定义字符串类型

```typescript
let name:string="jack"
let age:number=16
let sayHello:string=`hello,my name is ${name},I'll be ${age+1} years old next year`
```

***

### 空值

**JavaScript**没有空值(**void**)的概念，在**TypeScript**中表示没有任何返回值的函数

```typescript
function alertName():void {
    alert('my name is jack')
}
```

声明一个**void**类型的变量没啥用，你只能将他赋值为**undefined**和**null**

```typescript
let unusable:void=undefined
```

***

### Null和Undefined

在TypeScript中使用**null**和**undefined**来定义这两个原始数据类型

```typescript
let u:undefined=undefined
let n:null=null
```

与**void**不同的是**null**和**undefined**是所有类型的子类型，例如**undefined**类型可以赋值给**number**类型

而**void**类型不能赋值给**number**类型

```typescript
let num:number=undefined

let u:undefined
let num:number=u

let v:void
let num:number=v
// Type 'orror' is not assignable to type number
```

***

## 元组类型

数组合并了相同类型的对象，而元组**Tuple**合并了不同类型的对象

### 基础用法

定义了一对值分别为**string**和**number**的元组

```typescript
let jack:[string,number]=['jack',16]
```

当赋值或访问一个已知索引的元素时，会得到正确的类型

```typescript
let jack:[string,number]
jack[0]='jack'
jack[1]=16

jack[0].slice(1)
jack[1].toFixed(2)

//也可以只赋值一项
let tom: [string, number]
tom[0] = 'tom'
```

但是当对元组类型的变量初始化或直接赋值的时候，需要提供所有元组类型中指定的项

```typescript
let jack:[string,number]
jack=['jack',16]

let jack:[string,number]
jack=['jack']
// Property '1' is missing in type '[string]' but required in type '[string, number]'
```

***

### 越界的元素

当添加越界的元素时，它的类型会被限制为元组中每个类型的联合类型

```typescript
let jack:[string,number]
jack=['jack',16]
jack.push('candy')
jack.push(true)
// Argument of type 'true' is not assignable to parameter of type 'string | number'
```

***

## 枚举类型

### 基础用法

枚举使用**enum**关键字来定义

```typescript
enum Days {Sun,Mon,Tue,Wed,Thus,Fri,Sat}
```

枚举成员会被赋值从**0**开始递增的数字，同时也会对枚举值到枚举名进行反向映射

```typescript
enum Days {Sun,Mon,Tue,Wed,Thus,Fri,Sat}

console.log(Days['Sun'] === 0) // true
console.log(Days['Mon'] === 1) // true
console.log(Days['Tue'] === 2) // true
console.log(Days['Sat'] === 6) // true
console.log(Days[0] === 'Sun') // true
console.log(Days[1] === 'Mon') // true
console.log(Days[2] === 'Tue') // true
console.log(Days[6] === 'Sat') // true
```

上面的代码会被编译成

```javascript
var Days
(function(Days) {
  Days[(Days['Sun'] = 0)] = 'Sun'
  Days[(Days['Mon'] = 1)] = 'Mon'
  Days[(Days['Tue'] = 2)] = 'Tue'
  Days[(Days['Wed'] = 3)] = 'Wed'
  Days[(Days['Thu'] = 4)] = 'Thu'
  Days[(Days['Fri'] = 5)] = 'Fri'
  Days[(Days['Sat'] = 6)] = 'Sat'
})(Days || (Days = {}))
```

**Days['Sun'] = 0**的值是**0**，以此来进行反向映射

***

### 手动赋值

我们可以给枚举项手动赋值

```typescript
enum Days { Sun=7, Mon=1, Tue, Wed, Thus, Fri, Sat }

console.log(Days['Sun'] === 7) // true
console.log(Days['Mon'] === 1) // true
console.log(Days['Tue'] === 2) // true
console.log(Days['Sat'] === 6) // true
```

为手动赋值的枚举项会接着上一个枚举项递增

如果未手动赋值的枚举项与手动赋值的重复了，**TypeScript**是不会察觉到的

```typescript
enum Days { Sun = 3, Mon = 1, Tue, Wed, Thu, Fri, Sat }
console.log(Days['Sun'] === 3) // true
console.log(Days['Wed'] === 3) // true
console.log(Days[3] === 'Sun') // false
console.log(Days[3] === 'Wed') // true
```

递增到 **3** 的时候与前面的 **Sun** 的取值重复了，但是 **TypeScript** 并没有报错，导致 **Days[3]** 的值先是 **Sun**，而后又被 **Wed** 覆盖了

枚举项取值不会被覆盖，但是值取枚举项会被覆盖

手动赋值的枚举项可以不是数字，此时需要使用类型断言来让tsc无视类型检查

```typescript
enum Days {Sun=7, Mon, Tue, Wed, Thu, Fri, Sat=<any>'S'}

var Days
(function(Days) {
  Days[(Days['Sun'] = 7)] = 'Sun'
  Days[(Days['Mon'] = 8)] = 'Mon'
  Days[(Days['Tue'] = 9)] = 'Tue'
  Days[(Days['Wed'] = 10)] = 'Wed'
  Days[(Days['Thu'] = 11)] = 'Thu'
  Days[(Days['Fri'] = 12)] = 'Fri'
  Days[(Days['Sat'] = 'S')] = 'Sat'
})(Days || (Days = {}))
```

手动赋值的枚举项可以是小数或负数，此时后续未手动赋值的项的递增步长仍为**1**

```typescript
enum Days {  Sun = 7, Mon = 1.5, Tue, Wed, Thu, Fri, Sat }
console.log(Days['Sun'] === 7) // true
console.log(Days['Mon'] === 1.5) // true
console.log(Days['Tue'] === 2.5) // true
console.log(Days['Sat'] === 6.5) // true

enum Days {  Sun = 7, Mon = -1.5, Tue, Wed, Thu, Fri, Sat }
console.log(Days['Sun'] === 7); // true
console.log(Days['Mon'] === -1.5); // true
console.log(Days['Tue'] === -0.5); // true
console.log(Days['Sat'] === 3.5); // true
```

***

### 常数项和计算所得项

枚举项有两种类型:**常数项**和**计算所得项**

上面的都是常数项，一个典型的计算所得项的列子

```typescript
enum Color { Read, Green, Blue='Blue'.length }
```

**"blue".length**就是一个计算所得项

但是不能在计算所得项后面放入未手动赋值的项，那么他会因为获得不到初始值报错

```typescript
enum Color { Red = 'red'.length, Green, Blue }
// index.ts(1,33): error TS1061: Enum member must have initializer.
// index.ts(1,40): error TS1061: Enum member must have initializer.
```

***

### 常数枚举

常数枚举是使用`const enum`定义的枚举类型

```typescript
const enum Directions { Up, Down, Left, Right }
let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right];
```

常数枚举与普通枚举的区别是，**他会在编译阶段被删除**，并且不能包含计算成员

上述代码编译结果为

```typescript
var directions = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
```

***

### 外部枚举

外部枚举是使用`declare enum`定义的枚举类型

在 TypeScript 中，`declare` 是一个关键字，用于告诉编译器某些变量已经存在，但是这些变量的具体定义并不在当前 TypeScript 代码文件中。它通常用于声明外部的资源，例如全局变量、函数、类、枚举等，`declare` 定义的类型**只会用于编译时的检查**，编译结果中会被删除

```typescript
declare enum Directions {Up, Down, Left, Right}
let directions=[Directions.Up, Directions.Down, Directions.Left, Directions.Right]
```

上述代码编译结果为

```typescript
var directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right];
```

外部枚举与声明语句一样，常出现在声明文件中。

同时使用 `declare` 和 `const` 也是可以的：

```typescript
declare const enum Directions { Up, Down, Left, Right }

let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right];
```

编译结果：

```typescript
var directions = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
```

***

## 任意类型

任意类型（Any）用来表示允许赋值为任意类型。

如果是一个普通类型，在赋值过程中改变类型是不被允许的。

```ts
let myFavoriteNumber: string = 'seven';
myFavoriteNumber = 7;

// index.ts(2,1): error TS2322: Type 'number' is not assignable to type 'string'.
```

### 任意值的属性和方法

在任意值上访问任何属性都是允许的：

```ts
let anyThing: any = 'hello';

console.log(anyThing.myName);
console.log(anyThing.myName.firstName);
```

也允许调用任何方法：

```ts
let anyThing: any = 'Tom';

anyThing.setName('Jerry');
anyThing.setname('Jerry').sayHello();
anyThing.myName.setFirstName('Cat');
```

可以认为，声明一个变量为任意值之后，对它的任何操作，返回的内容的类型都是**任意值**。

***

### 未声明类型的变量

变量如果在声明的时候，未指定其类型，那么它会被识别为任意值类型：

```ts
let something;
something = 'seven';
something = 7;

something.setName('Tom');
```

等价于：

```ts
let something: any;
something = 'seven';
something = 7;

something.setName('Tome');
```

***

## never类型

`never` 类型同时也是 TypeScript 中的底层类型，下列是一些自然被分配的例子：

- 一个从来不会有返回值的函数（如：函数内含有 `while(true) {}`）
- 一个总是会抛出错误的函数（如：`function foo() { throw new Error('Not Implemented') }`，`foo` 的返回类型是 `never`）

```typescript
function infiniteloop(): never {
  while (true) {}
}
function error(message: string): never {
  throw Error('message');
}
function fail() {
  return error('Something wrong happen.');
}
```

函数运行不到结束或是抛出错误，会被分配never

***

### 与`void`的差异

一旦有人告诉你，`never` 表示一个从来不会优雅的返回的函数时，你可能马上就会想到与类似的 `void`，然而实际上，`void` 表示没有任何类型，`never` 表示永远不存在的值的类型。

当一个函数没有返回值时，它返回了一个 `void` 类型，但是，当一个函数根本就没有返回值时（或者总是抛出错误），它返回了一个 `never`，`void` 指可以被赋值的类型（在 `strictNullChecking` 为 `false` 时），但是 `never` 不能赋值给其他任何类型，除了 `never`。

***

## 数组的类型

### 数组成员类型

最简单的方法是使用「类型 + 方括号」来表示数组,数组的项中不允许出现其他的类型

```typescript
let arr:number[]=[1,2,3]

let fibonacci: number[] = [1, '1', 2, 3, 5];
// Type 'string' is not assignable to type 'number'.
```

数组的一些方法的参数也会根据数组在定义时约定的类型进行限制

```ts
let fibonacci: number[] = [1, 1, 2, 3, 5];
fibonacci.push('8');

// Argument of type '"8"' is not assignable to parameter of type 'number'.
```

### 数组泛型

Array<elemType>来表示数组

```typescript
// 表示声明的数组必须是数字类型
let fibonacci: Array<number> = [1, 1, 2, 3, 5];
// 表示声明的数组可以是任意类型
let foo: Array<any>;
// 表示声明的数组元素必须是包含 name 与 age 的对象，并且 name 为字符串，age 为数字
let bar: Array<{name: string; age: number}>;
// 表示数组元素必须为 name 的对象爱哪个，age 可选
let baz: Array<{name: string; age?: number}>
```

### 用接口表示数组

```typescript
interface NumberArray {
    [index:number]:number
}
let numArr:NumberArray=[1,2,3]
```

`NumberArray` 表示：只要索引的类型是数字时，那么值的类型必须是数字。

虽然接口也可以用来描述数组，但是我们一般不会这么做，因为这种方式比前两种方式复杂多了。

***

### 类数组

类数组（Array-like Object）不是数组类型，比如 `arguments`：

```ts
function sum() {
  let args: number[] = arguments;
}

// Type 'IArguments' is missing the following properties from type 'number[]' : pop, push, concat, join, and 24 more.
```

上例中，`arguments` 实际上是一个类数组，不能用普通的数组方式来描述，而应该用接口。

```ts
function sum() {
  let args: {
    [index: number]: number;
    length: number;
    calle: Funcition;
  } = arguments;
}
```

在这个例子中，我们除了约束当索引的类型是数字时，值的类型必须是数字之外，也约束了它还有 `length` 和 `callee` 两个属性。

事实上常用的累数组都有自己的接口定义，如 `IArguments`、`NodeList`、`HTMLCollection` 等。

```ts
function sum() {
  let args : IArguments = arguments;
}
```

其中 `IArguments` 是 TypeScript 中定义好了的类型，它实际上是：

```ts
interface IArguments {
  [index: number]: any;
  length: number;
  callee: musi;
}
```

***

### 任意值在数组中的应用

一个比较常见的做法是，用 `any` 表示数组中允许出现任意类型：

```ts
let list = any[] = ['xcailiu', 25 { website: 'http://'}]
```

***

## 函数的类型

在 JavaScript 中，有两种常见的定义函数方式：

- 函数声明（Function Declaration）
- 函数表达式（Function Expression）

### 函数声明

一个函数有输入和输出，要在 TypeScript 中对其进行约束，需要把输入和输出都考虑到，其中函数声明的类型定义较简单：

```ts
function sum(x: number, y: number): number {
  return x + y;
}
```

注意，**输入多余的（或者少于要求的）参数，是不被允许的**：

```ts
function sum(x: number, y: number): number {
  return x + y;
}
sum(1, 2, 3);

// index.ts(4,1): error TS2346: Supplied parameters do not match any signature of call target.
function sum(x: number, y: number): number {
  return x + y;
}
sum(1);

// index.ts(4,1): error TS2346: Supplied parameters do not match any signature of call target.
```

***

### 函数表达式

如果要我们现在写一个对函数表达式（Function Expression）的定义，可能会写成这样：

```ts
let mySum = function(x: number, y: number): number {
  return x + y;
};
```

这是可以通过编译的，不过事实上，上面的代码只对等号右侧的匿名函数进行了类型定义，而等号左边的 `mySum`，是通过赋值操作进行类型推论而推断出来的。如果需要我们手动给 `mySum` 添加类型，则应该是这样：

```ts
let mySum: (x: number, y: number) => number = function(x: number, y: number): number {
  return x + y;
};
```

注意不要混淆了 TypeScript 中的 `=>` 和 ES6 中的 `=>`。

在 TypeScript 的类型定义中，`=>` 用来表示函数的定义，左边是输入类型，需要用括号括起来，右边是输出类型。

在 ES6 中，`=>` 叫做箭头函数

### 用接口定义函数的形状

我们也可以使用接口的方式来定义一个函数需要符合的形状：

```ts
interface SearchFunc {
  (source: string, subString: string): boolean;
}

let mySearch: SearchFunc;
mySearch = function(source: string, subString: string) {
  return source.search(subString) !== -1;
};
```

### 可选参数

前面提到，输入多余的（或者少于要求的）参数，是不允许的。那么如何定义可选的参数呢？

与接口中的可选属性类似，我们用 `?` 表示可选的参数：

```ts
function buildName(firstName: string, lastName?: string) {
  if (lastName) {
    return firstName + ' ' + lastName;
  } else {
    return firstName;
  }
}

let tomcat = buildName('Tom', 'Cat');
let tom = buildName('Tom');
```

需要注意的是，可选参数必须接在必需参数后面。换句话说，可选参数后面不允许再出现必需参数了：

```ts
function buildName(firstName?: string, lastName: string) {
  if (firstName) {
    return firstName + ' ' + lastName;
  } else {
    return lastName;
  }
}

let tomcat = buildName('Tom', 'Cat');
let tom = buildName(undefined, 'Tom');

// index.ts(1,40): error TS1016: A required parameter cannot follow an optional parameter.
```

### 参数默认值

在 ES6 中，我们允许给函数的参数添加默认值，TypeScript 会将添加了默认值的参数识别为可选参数：

```ts
function buildName(firstName: string, lastName: string = 'Cat') {
  return firstName + ' ' + lastName;
}

let tomcat = buildName('Tom', 'Cat');
let tom = buildName('Tom');
```

默认参数后面可以跟普通参数：

```ts
function buildName(firstName: string = 'Tom', lastName: string) {
  return firstName + ' ' + lastName;
}

let tomcat = buildName('Tom', 'Cat');
let cat = buildName(undefined, 'Cat');
```

### 剩余参数

在 ES6 中，可以使用 `...rest` 的方式获取函数中的剩余参数（`rest` 参数）：

```ts
function push(array, ...items) {
  items.forEach(function(item) {
    array.push(item);
  });
}

let a = [];
push(a, 1, 2, 3);
```

事实上，`items` 是一个数组。所以我们可以用数组的类型来定义它：

```ts
function push(array: any[], ...items: any[]) {
  items.forEach(function(item) {
    array.push(item);
  });
}

let a = [];
push(a, 1, 2, 3);
```

***

### 重载

重载允许一个函数接受不同数量或类型的参数时，作出不同的处理。

比如，我们需要实现一个函数 `reverse`，输入数字 `123` 的时候，输出反转的数字 `321`，输入字符串 `'hello'` 的时候，输出反转的字符串 `'olleh'`。

利用联合类型，我们可以这么实现：

```typescript
function reverse(x: number | string): number | string | void {
  if (typeof x === 'number') {
    return Number(x.toString().split('').reverse().join('')
    )
  } else if (typeof x === 'string') {
    return x.split('').reverse().join('')
  } else {
    return
  }
}
```

然而这样有一个缺点，就是不能够精确的表达，输入为数字的时候，输出也应该为数字，输入为字符串的时候，输出也应该为字符串。

这时，我们可以使用重载定义多个 `reverse` 的函数类型：

```ts
function reverse(x: number): number;
function reverse(x: string): string;
function reverse(x: number | string): number | string {
  if (typeof x === 'number') {
    return Number(
      x
        .toString()
        .split('')
        .reverse()
        .join('')
    );
  } else if (typeof x === 'string') {
    return x
      .split('')
      .reverse()
      .join('');
  }
}
```

上例中，我们重复定义了多次函数 reverse，前几次都是函数定义，最后一次是函数实现。在编辑器的代码提示中，可以正确的看到前两个提示。

注意，TypeScript 会优先从最前面的函数定义开始匹配，所以多个函数定义如果有包含关系，需要优先把精确的定义写在前面。

***

## 对象的类型/接口

接口是对象的类型。

TypeScript 的核心原则之一是对值具有结构进行类型检查。它有时被称作「鸭式辨型」或「结构性子类型化」。在 TypeScript 里，接口的作用就是为这些类型命名和为你的代码或第三方代码定义契约

### 基础用法

```ts
interface Person {
  name: string;
  age: number;
}

let tom: Person = {
  name: 'Tom',
  age: 25,
};
```

***

上面的例子中，我们定义了一个接口 Person，接着定义了一个变量 `tom`，它的类型是 `Person`。这样，我们就约束了 `tom` 的形状必须和接口 `Person` 一致。

接口一般首字母大写。有的编程语言中会建议接口的名称加上 `I` 前缀。

定义的变量比接口少了一些属性是不允许的：

```ts
interface Person {
    name: string;
    age: number;
}

let tom: Person = {
    name: 'Tom
}
// index.ts(6,5): error TS2322: Type '{ name: string; }' is not assignable to type 'Person'.
// Property 'age' is missing in type '{ name: string; }'.
```

多一些属性也是不允许的：

```ts
interface Person {
  name: string;
  age: number;
}

let tom: Person = {
  name: 'Tom',
  age: 25,
  gender: 'male',
};

// index.ts(9,5): error TS2322: Type '{ name: string; age: number; gender: string; }' is not assignable to type 'Person'.
//   Object literal may only specify known properties, and 'gender' does not exist in type 'Person'.
```

可见，赋值的时候，变量的形状必须和接口保持一致。

***

### 可选属性

有时我们希望不要完全匹配一个形状，那么可以用可选属性：

```ts
interface Person {
  name: string;
  age?: number;
}

let tom: Person = {
  name: 'Tom',
};
interface Person {
  name: string;
  age?: number;
}

let tom: Person = {
  name: 'Tom',
  age: 25,
};
```

可选属性的含义是该属性可以不存在。

这时仍然不允许添加未定义的属性：

```ts
interface Person {
  name: string;
  age?: number;
}

let tom: Person = {
  name: 'Tom',
  age: 25,
  gender: 'male',
};

// examples/playground/index.ts(9,5): error TS2322: Type '{ name: string; age: number; gender: string; }' is not assignable to type 'Person'.
//   Object literal may only specify known properties, and 'gender' does not exist in type 'Person'.
```

这时仍然不允许添加未定义的属性。

***

### 任意属性

有时候我们希望一个接口允许有任意的属性，可以使用如下方式：

```ts
interface Person {
  name: string;
  age?: number;
  [propName: string]: any;
}
```

使用 `[propName: string]` 定义了任意属性取 `string` 类型的值。

需要注意的是，一旦定义了任意属性，那么确定属性和可选属性的参加类型都必须是它的类型的子集：

```ts
interface Person {
    name: string;
    age?: number;
    [prop:string]: string;
}

let tom: Person={
    name: 'Tom',
    age: 25,
    gender: 'male'
}

// index.ts(3,5): error TS2411: Property 'age' of type 'number' is not assignable to string index type 'string'.
// index.ts(7,5): error TS2322: Type '{ [x: string]: string | number; name: string; age: number; gender: string; }' is not assignable to type 'Person'.
//   Index signatures are incompatible.
//     Type 'string | number' is not assignable to type 'string'.
//       Type 'number' is not assignable to type 'string'.
```

上例中，任意属性的值允许是 `string`，但是可选属性 `age` 的值却是 `number`，`number` 不是 `string` 的子属性，所以报错了。

另外，在报错信息中可以看出，此时 `{ name: 'Tom', age: 25, gender: 'male' }` 的类型被推断成了 `{ [x: string]: string | number; name: string; age: number; gender: string; }`，这是联合类型和接口的结合。

***

### 只读属性

有时候我们希望对象中的一些字段只能在创建的时候被赋值，那么可以用 `readonly` 定义只读属性：

```ts
interface Person {
  readonly id: number;
  name: string;
  age?: number;
  [propName: string]: any;
}

let tom: Person = {
  id: 89757,
  name: 'Tom',
  gender: 'male',
};

tom.id = 9527;

// index.ts(14,5): error TS2540: Cannot assign to 'id' because it is a constant or a read-only property.
```

上例中，使用 `readonly` 定义的属性 `id` 初始化后，又被赋值了，所以报错了。

注意，只读的约束存在于第一次给对象赋值的时候，而不是第一次给只读属性赋值的时候：

```ts
interface Person {
  readonly id: number;
  name: string;
  age?: number;
  [propName: string]: any;
}

let tom: Person = {
  name: 'Tom',
  gender: 'male',
};

tom.id = 89757;

// index.ts(8,5): error TS2322: Type '{ name: string; gender: string; }' is not assignable to type 'Person'.
//   Property 'id' is missing in type '{ name: string; gender: string; }'.
// index.ts(13,5): error TS2540: Cannot assign to 'id' because it is a constant or a read-only property.
```

上例中，报错信息有两处，第一处是在对 `tom` 进行赋值的时候，没有给 `id` 赋值。

第二处是在给 `tom.id` 赋值的时候，由于它是只读属性，所以报错了。

***

## 类

### 属性和方法

使用 `class` 定义类，使用 `constructor` 定义构造函数。

通过 `new` 生成新实例的时候，会自动调用构造函数。

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  sayHi() {
    return `My name is ${this.name}`;
  }
}

let a = new Animal('Jack');
console.log(a.sayHi()); // My name is Jack
```

***

### 类的继承

使用 `extends` 关键字实现继承，子类中使用 `super` 关键字来调用父类的构造函数和方法。

```js
class Cat extends Animal {
  constructor(name) {
    super(name); // 调用父类的 constructor(name)
    console.log(this.name);
  }
  sayHi() {
    return 'Meow, ' + super.sayHi(); // 调用父类的 sayHi()
  }
}

let c = new Cat('Tom'); // Tom
console.log(c.sayHi()); // Meow, My name is Tom
```

***

### 存取器

使用 `getter` 和 `setter` 可以改变属性的赋值和读取行为：

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  get name() {
    return 'Jack';
  }
  set name(value) {
    console.log('setter: ' + value);
  }
}

let a = new Animal('Kitty'); // setter: Kitty
a.name = 'Tom'; // setter: Tom
console.log(a.name); // Jack
```

***

### 静态方法

使用 `static` 修饰符修饰的方法称为静态方法，它们不需要实例化，而是直接通过类来调用。

```js
class Animal {
  static isAnimal(a) {
    return a instanceof Animal;
  }
}

let a = new Animal('Jack');
Animal.isAnimal(a); // true
a.isAnimal(a); // TypeError: a.isAnimal is not a function
```

***

### 使用方法

#### 访问修饰符

TypeScript 可以使用三种访问修饰符（Access Modifiers），分别是 `public`、`private` 和 `protected`。

- `public` 修饰的属性或方法是**公有的**，可以在任何地方被访问到，默认所有的属性和方法都是 `public` 的
- `private` 修饰的属性或方法是**私有的**，不能在声明它的类的外部访问
- `protected` 修饰的属性或方法是**受保护的**，它和 `private` 类似，区别是它在子类中也是允许被访问的

下面举一些例子：

```ts
class Animal {
  public name;
  public constructor(name) {
    this.name = name;
  }
}

let lion = new Animal('Jack');
console.log(lion.name); // Jack
lion.name = 'Tom';
console.log(lion.name); // Tom
```

上面的例子中，`name` 被设置为了 `public`，所以直接访问实例的 `name` 属性是允许的。

很多时候，我们希望有的属性是无法直接存取的，这时候就可以用 `private` 了：

```ts
class Animal {
  private name;
  public constructor(name) {
    this.name = name;
  }
}

let lion = new Animal('Jack');
console.log(lion.name); // Jack

lion.name = 'Tom'; // 无法直接存储 name 属性

// index.ts(9,13): error TS2341: Property 'name' is private and only accessible within class 'Animal'.
// index.ts(10,1): error TS2341: Property 'name' is private and only accessible within class 'Animal'.
```

需要注意的是，TypeScript 编译之后的代码中，并没有限制 `private` 属性在外部的可访问性。

上面的例子编译后的代码是：

```js
var Animal = (function () {
  function Animal(name {
    this.name = name;
  })
  return Animal;
}());

var lion = new Animal('Jack');
console.log(lion.name);
lion.name = 'Tom';
```

使用 `private` 修饰的属性或方法，在子类中也是不允许访问的。

```ts
class Animal {
  private name;
  public constructor(name) {
    this.name = name;
  }
}

class Cat extends Animal {
  constructor(name) {
    super(name);
    console.log(this.name);
  }
}

// index.ts(11,17): error TS2341: Property 'name' is private and only accessible within class 'Animal'.
```

而如果是用 `protected` 修饰，则允许在子类中访问：

```ts
class Animal {
  protected name;
  public constructor(name) {
    this.name = name;
  }
}

class Cat extends Animal {
  constructor(name) {
    super(name);
    console.log(this.name);
  }
}
```

当构造函数修饰为 `private` 时，该类不允许被继承或实例化：

```ts
class Animal {
  public name;
  private constructor(name) {
    this.name = name;
  }
}
class Cat extends Animal {
  constructor(name) {
    super(name);
  }
}

let a = new Animal('Jack');

// index.ts(7,19): TS2675: Cannot extend a class 'Animal'. Class constructor is marked as private.
// index.ts(13,9): TS2673: Constructor of class 'Animal' is private and only accessible within the class declaration.
```

总结：

- public 公有属性
  - 可以在任何地方被访问到
- private 私有属性
  - 实例对象无法直接存取
  - 子类不允许访问
  - 修饰构造函数时，该类不允许被继承或实例化
- protected 保护属性
  - 允许子类访问
  - 修饰构造函数时，该类只允许继承

#### 参数属性

修饰符和 `readonly` 还可以使用在构造函数参数中，等同于类中定义该属性同时给该属性赋值，使代码更简洁。

```ts
class Animal {
  // public name: string
  public constructor(public name) {
    // this.name = name;
  }
}
```

***

#### 只读修饰符

只读属性关键字，只允许出现在**属性声明**或**索引签名**或**构造函数**中。

```ts
class Animal {
  readonly name;
  public constructor(name) {
    this.name = name;
  }
}

let lion = new Animal('Jack');
console.log(lion.name); // Jack
lion.name = 'Tom';

// index.ts(10,3): TS2540: Cannot assign to 'name' because it is a read-only property.
```

注意如果 `readonly` 和其他访问修饰符同时存在的话，需要写在其后面。

```ts
class Animal {
  // public readonly name;
  public constructor(public readonly name) {
    // this.name = name;
  }
}
```

***

#### 抽象类

`abstract` 用于定义抽象类和其中的抽象方法。

什么是抽象类？

首先，抽象类是不允许被实例化的：

```ts
abstract class Animal {
  public name;
  public constructor(name) {
    this.name = name;
  }
  public abstract sayHi();
}

let a = new Animal('Jack');

// index.ts(9,11): error TS2511: Cannot create an instance of the abstract class 'Animal'.
```

上面的例子中，我们定义了一个抽象类 `Animal`，并且定义了一个抽象方法 `sayHi`。在实例化抽象类的时候报错了。

⚠️ **注意**：其次，抽象类中的抽象方法必须被子类实现：

```ts
abstract class Animal {
  public name;
  public constructor(name) {
    this.name = name;
  }
  public abstract sayHi();
}

class Cat extends Animal {
  public eat() {
    console.log(`${this.name} is eating.`);
  }
}

let cat = new Cat('Tom');

// index.ts(9,7): error TS2515: Non-abstract class 'Cat' does not implement inherited abstract member 'sayHi' from class 'Animal'.
```

上面的例子中，我们定义了一个类 Cat 继承了抽象类 Animal，但是没有实现抽象方法 sayHi，所以编译报错了。

下面是一个正确使用抽象类的例子：

```ts
abstract class Animal {
  public name;
  public constructor(name) {
    this.name = name;
  }
  public abstract sayHi();
}

class Cat extends Animal {
  public sayHi() {
    console.log(`Meow, My name is ${this.name}`);
  }
}

let cat = new Cat('Tom');
```

上面的例子中，我们实现了抽象方法 `sayHi`，编译通过了。

需要注意的是，即使是抽象方法，TypeScript 的编译结果中，仍然会存在这个类，上面的代码的编译结果是：

```js
var __extends =
  (this && this.__extends) ||
  function(d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() {
      this.constructor = d;
    }
    d.prototype = b === null ? Object.create(b) : ((__.prototype = b.prototype), new __());
  };
var Animal = (function() {
  function Animal(name) {
    this.name = name;
  }
  return Animal;
})();
var Cat = (function(_super) {
  __extends(Cat, _super);
  function Cat() {
    _super.apply(this, arguments);
  }
  Cat.prototype.sayHi = function() {
    console.log('Meow, My name is ' + this.name);
  };
  return Cat;
})(Animal);
var cat = new Cat('Tom');
```

***

### 类的类型

给类加上 TypeScript 的类型很简单，与接口类似：

```ts
class Animal {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  sayHi(): string {
    return `My name is ${this.name}`;
  }
}

let a: Animal = new Animal('Jack');
console.log(a.sayHi()); // My name is Jack
```

***

## 类型别名

类型别名用来给一个类型起个新名字。

```ts
type Name = string;
type NameResolver = () => string;
type NameOrResolver = Name | NameResolver;

function getName(n: NameOrResolver): Name {
  if (typeof n === 'string') {
    return n;
  } else {
    return n();
  }
}
```

上例中，我们使用 `type` 创建类型别名。

类型别名常用于联合类型。

***

## 声明合并

如果定义了两个相同名字的函数、接口或类，那么它们会合并成一个类型。

### 函数的合并

函数重载

### 接口的合并

接口中的属性在合并时会简单的合并到一个接口中：

```ts
interface Alarm {
  price: number;
}
interface Alarm {
  weight: number;
}
```

相当于：

```ts
interface Alarm {
  price: number;
  weight: number;
}
```

注意，合并的属性的类型必须是唯一的：

```ts
interface Alarm {
  price: number;
}
interface Alarm {
  price: number; // 虽然重复了，但是类型都是 `number`，所以不会报错
  weight: number;
}
interface Alarm {
  price: number;
}
interface Alarm {
  price: string; // 类型不一致，会报错
  weight: number;
}

// index.ts(5,3): error TS2403: Subsequent variable declarations must have the same type.  Variable 'price' must be of type 'number', but here has type 'string'.
```

接口中方法的合并，与函数的合并一样：

```ts
interface Alarm {
  price: number;
  alert(s: string): string;
}
interface Alarm {
  weight: number;
  alert(s: string, n: number): string;
}
```

相当于：

```ts
interface Alarm {
  price: number;
  weight: number;
  alert(s: string): string;
  alert(s: string, n: number): string;
}
```

***

## 泛型

泛型（Generics）是指在定义函数、接口或类的时候，不预先指定具体的类型，而在使用的时候再指定类型的一种特性。

### 基础用法

首先，我们来实现一个函数 `createArray`，它可以创建一个指定长度的数组，同时将每一项都填充一个默认值：

```ts
function createArray(length: number, value: any): Array<any> {
  let result = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
}

createArray(3, 'x'); // ['x', 'x', 'x']
```

上例中，我们使用了之前提到过的数组泛型来定义返回值的类型。

这段代码编译不会报错，但是一个显而易见的缺陷是，它并没有准确的定义返回值的类型：

`Array<any>` 允许数组的每一项都为任意类型。但是我们预期的是，数组中每一项都应该是输入的 `value` 的类型。

这时候，泛型就派上用场了：

```ts
function createArray<T>(length: number, value: T): Array<T> {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
}

createArray<string>(3, 'x'); // ['x', 'x', 'x']
```

上例中，我们在函数名后添加了 `<T>`，其中 `T` 用来指代任意输入的类型，在后面的输入 `value: T` 和输出 `Array<T>` 中即可使用了。

***

### 多个类型的参数

定义泛型的时候，可以一次定义多个类型参数：

```ts
function swap<T, U>(tuple: [T, U]): [U, T] {
  return [tuple[1], tuple[0]];
}

swap([7, 'seven']); // ['seven', 7]
```

***

### 泛型约束

在函数内部使用泛型变量的时候，由于事先不知道它是哪种类型，所以不能随意的操作它的属性或方法：

```ts
function loggingIdentity<T>(arg: T): T {
  console.log(arg.length);
  return arg;
}

// index.ts(2,19): error TS2339: Property 'length' does not exist on type 'T'.
```

上例中，泛型 `T` 不一定包含属性 `length`，所以编译的时候报错了。

这时，我们可以对泛型继续给你约束，只允许这个函数传入那些包含 `length` 属性的变量。这就是**泛型约束**：

```ts
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}
```

上例中，我们使用了 `extends` 约束了泛型 `T` 必须符合接口 `Lengthwise` 的形状，也就是必须包含 `length` 属性。

此时如果调用 `loggingIdentity` 的时候，传入的 `arg` 不包含 `length`，那么在编译阶段就会报错了：

```ts
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}

loggingIdentity(7);

// index.ts(10,17): error TS2345: Argument of type '7' is not assignable to parameter of type 'Lengthwise'.
```

多个类型参数之间也可以互相约束：

```ts
function copyFields<T extends U, U>(target: T, source: U): T {
  for (let id in source) {
    target[id] = (<T>source)[id];
  }
  return target;
}

let x = { a: 1, b: 2, c: 3, d: 4 };

copyFields(x, { b: 10, d: 20 });
```

上例中，我们使用了两个类型参数，其中要求 T 继承 U，这样就保证了 U 上不会出现 T 中不存在的字段。

***

### 泛型接口

可以使用接口的方式来定义一个函数需要符合的形状：

```ts
interface SearchFunc {
  (source: string, subString: string): boolean;
}

let mySearch: SearchFunc;
mySearch = function(source: string, subString: string) {
  return source.search(subString) !== -1;
};
```

当然也可以使用含有泛型的接口来定义函数的形状：

```ts
interface CreateArrayFunc {
  <T>(length: number, value: T): Array<T>;
}

let createArray: CreateArrayFunc;
createArray = function<T>(length: number, value: T): Array<T> {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
};

createArray(3, 'x'); // ['x', 'x', 'x']
```

进一步，我们可以把泛型参数提前到接口名上：

```ts
interface CreateArrayFunc<T> {
  (length: number, value: T): Array<T>;
}

let createArray: CreateArrayFunc<any>;
createArray = function<T>(length: number, value: T): Array<T> {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
};

createArray(3, 'x'); // ['x', 'x', 'x']
```

⚠️ 注意，此时在使用泛型接口的时候，需要定义泛型的类型。

***

### 泛型类

与泛型接口类似，泛型也可以用于类的类型定义中：

```ts
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber = add;
```

***

### 泛型参数的默认类型

在 TypeScript 2.3 之后，我们可以为泛型中的类型参数指定类型。当使用泛型时没有代码中直接指定类型参数，从实际值参数中也无法推测出时，这个默认类型就会起起作用。

```ts
function createArray<T = string>(length: number, value: T): Array<T> {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
}
```

***

## 类型断言

类型断言（Type Assertion）可以用来手动指定一个值的类型。

### 语法

```ts
<类型>值;

// 或

值 as 类型;
```

在 tsx 语法（React 的 JSX 语法的 TS 版）中必须用后一种。

***

### 示例

示例：将一个联合类型的变量指定为一个更加具体的类型

当 TypeScript 不确定一个联合类型到底是哪个类型的时候，我们只能访问此联合类型的所有类型里共有的属性或方法：

```ts
function getLength(something: string | number): number {
  return something.length;
}

// index.ts(2,22): error TS2339: Property 'length' does not exist on type 'string | number'.
//   Property 'length' does not exist on type 'number'.
```

而有时候，我们确实需要在还不确定类型的时候就访问其中一个类型的属性或方法，比如：

```ts
function getLength(something: string | number): number {
  if (something.length) {
    return something.length;
  } else {
    return something.toString().length;
  }
}

// index.ts(2,19): error TS2339: Property 'length' does not exist on type 'string | number'.
//   Property 'length' does not exist on type 'number'.
// index.ts(3,26): error TS2339: Property 'length' does not exist on type 'string | number'.
//   Property 'length' does not exist on type 'number'.
```

上例中，获取 `something.length` 的时候会报错。

此时可以使用类型断言，将 `something` 断言成 `string`：

```ts
function getLength(something: string | number): number {
  if ((<string>something).length) {
    return (<string>something).length;
  } else {
    return something.toString().length;
  }
}
```

类型断言的用法加上，在需要断言的变量前加上 `<Type>` 即可。

类型断言不是类型转换，断言成一个联合类型中不存在的类型是不允许的。

```ts
function toBoolean(something: string | number): boolean {
  return <boolean>something;
}

// index.ts(2,10): error TS2352: Type 'string | number' cannot be converted to type 'boolean'.
//   Type 'number' is not comparable to type 'boolean'.
```

***

## 类型推论

如果没有明确的指定类型，那么 TypeScript 会依照类型推论（Type Inference）（又称类型推断、类型判断）的规则推断出一个类型。

以下代码虽然没有指定类型，但是会在编译的时候报错：

```ts
let num = 'seven';
num = 7;

// index.ts(2,1): error TS2322: Type 'number' is not assignable to type 'string'.
```

事实上，它等价于：

```ts
let num: string = 'seven';
num = 7;

// index.ts(2,1): error TS2322: Type 'number' is not assignable to type 'string'.
```

TypeScript 会在没有明确的指定类型的时候推测出一个类型，这就是类型推论。

如果定义的时候没有赋值，不管之后有没有赋值，都会被推断成 `any` 类型而完全不被类型检查：

```ts
let num;
num = 'seven';
num = 7;
```

***

## 类型保护

对于联合类型的变量，我们是无法知道编译时的具体类型的。JavaScript 中常用的方式是检查成员是否存在，但是 TypeScript 中联合类型只有访问联合类型中共同拥有的成员。

可是通过类型断言来进行类型判断，但是有个问题就是每个分支都需要进行类型判断。

TypeScript 的类型保护机制：一次判断，整个作用域/所有分支有效。

类型保护（Type Guards）就是一些表达式，会在运行时检查以确保在某个作用域内的类型。

### typeof类型保护

`typeof` 类型保护用于判断变量是哪种原始类型。

```ts
function fn(param: string | number) {
  if (typeof param === 'string') {
    console.log('string');
  }
  if (typeof param === 'number') {
    console.log('number');
  }
}
```

原本是联合类型，由于应用了 `typeof`，后面作用域的 `param` 就确定为 `number` 类型。

`typeof` 类型保护只有两种形式能被识别：

- `typeof val === 'typename'`
- `typeof val !== 'typename'`

`typename` 必须为 `number`、`string`、`boolean` 或 `symbol` 类型。

但是 TypeScript 并不会阻止与其他字符串比较，语言不会把那些表达式识别为类型保护。

***

### instanceof 类型保护

`instanceof` 类型保护和 `typeof` 类型保护用法相似，它主要用于判断是否是一个类的对象或继承对象的。

```ts
const foo: Date | RegExp;

if (foo instanceof RegExp) {
  // 正确 instanceof 类型保护，自动对应到 RegExp 实例类型
  foo.test('');
} else {
  // 正确 自动对应到 Date 实例类型
  foo.getTime();
}
interface DateOrRegExp {
  // 这里表示构造器无参，Date 类型的类
  new (): Date;
  new (value?: string): RegExp;
}

let Foo: DateOrRegExp;

let foo;
if (foo instanceof Foo) {
  // foo 从 any 到 RexExp | Date
  console.log(foo);
}
```

`instanceof` 类型保护是通过构造函数来细化类型，其右侧要求是一个构造函数，TypeScript 将细化为：

1. 此构造函数的 `prototype` 属性的类型，如果它的类型不为 `any`
2. 构造签名所返回类型的联合

### 自定义类型保护

`typeof` 和 `instanceof` 类型保护能够满足一般场景，对于一些更加特殊的，可以通过自定义类型保护来对应类型，比如我们自己定义一个请求参数的接口类型。

```ts
interface RequestParams {
  url: string;
  onSuccess?: () => void;
  onFailed?: () => void;
}

function isValidRequestParams(request: any): request is RequestParams {
  return request && request.url;
}

let request;
// 检测客户端发送过来的参数
if (isValidRequestParams(requst)) {
  request.url;
}
```

这里面通过判断，我们需要手动告诉编译器通过 `isValidRequestParams` 的判断则 `request` 就是 `RequestParams` 类型的参数，编译器通过类型谓词 `parameterName is Type` 得知，`isValidRequestParams` 返回了 `true` 则 `request` 就是 `RequestParams` 类型。

其他用法和上面所列举一致。

```ts
let isNumber: (value: any) => value is number;

let foo: string | number;
if (isNumber(foo)) {
  // 缩窄到 number
  foo.toFixed(2);
} else {
  // 通过类型保护，编译器知道不是 number 就是 string
  foo.toUpperCase();
}
```

***

## 类型兼容性

类型兼容性用于确定一个类型是否能赋值给其他类型。

如 `string` 类型与 `number` 类型不兼容：

```ts
let str: string = 'Hello world!';
let num: number = 123;

str = num; // Error: 'number' 不能赋值给 'string'
num = str; // Error: 'string' 不能赋值给 'number'
```

### 安全性

TypeScript 类型系统设计比较方便，它允许你有一些不正确的行为。例如：任何类型都能被赋值给 `any`，这意味着告诉编译器你可以做任何你想做的事情：

```ts
const foo: any = 123;
foo = 'hello';

foo.toPrecision(3);
```

***

### 结构化

TypeScript 对象是一种结构类型，这意味着只要结构匹配，名称也就无关紧要了：

```ts
interface Point {
  x: number;
  y: number;
}

class Point2D {
  constructor(public x: number, public y: number) {}
}

let p: Point;

// ok, 因为是结构化的类型
p = new Point2D(1, 2);
```

这允许你动态创建对象（就好像你在 vanilla JS 中使用一样），并且它如果能被推断，该对象仍然具有安全性。

```ts
interface Point2D {
  x: number;
  y: number;
}

interface Point3D {
  x: number;
  y: number;
  z: number;
}

const point2D: Point2D = { x: 0, y: 10 };
const point3D: Point3D = { x: 0, y: 10, z: 20 };
function iTakePoint2D(point: Point2D) {
  /* do something */
}

iTakePoint2D(point2D); // ok, 完全匹配
iTakePoint2D(point3D); // 额外的信息，没关系
iTakePoint2D({ x: 0 }); // Error: 没有 'y'
```

***

### 变体

对类型兼容性来说，变体是一个利于理解和重要的概念。

对一个简单类型 `Base` 和 `Child` 来说，如果 `Child` 是 `Base` 的子类，`Child` 的实例能被赋值给 `Base` 类型的变量。

在由 `Base` 和 `Child` 组合的复杂类型的类型兼容性中，它取决于相同场景下的 `Base` 与 `Child` 的变体：

- 协变（Covariant）：只在同一个方向
- 逆变（Contravariant）：只在相反的方向
- 双向协变（Bivariant）：包括同一个方向和不同方向
- 不变（Invariant）：如果类型不完全相同，则它们是不兼容的

> 对于存在完全可变数据的健全的类型系统（如 JavaScript），`Invariant` 是一个唯一的有效的可选变量，但是如我们说讨论的，便利性迫使我们作出一些不是很安全的选择。

***

### 函数

#### 返回类型

协变（Covariant）：返回类型必须包含足够的数据。

```ts
interface Point2D {
  x: number;
  y: number;
}

interface Point3D {
  x: number;
  y: number;
  z: number;
}

let iMakePoint2D = (): Point2D => ({ x: 0, y: 0 });
let iMakePoint3D = (): Point3D => ({ x: 0, y: 0, z: 0 });

iMakePoint2D = iMakePoint3D;
iMakePoint3D = iMakePoint2D; // ERROR: Point2D 不能赋值给 Point3D
```

***

#### 参数数量

更少的参数数量是好的（如：函数能够选择性地忽略一些多余的参数），但是你得保证有足够的参数被使用：

```ts
const foo = (x: (err: Error, data: any) => void) => {
  /* Do Something Else */
};

foo(() => null);
foo(err => null);
foo((err, data) => null);

// Error: 参数类型 `(err: any, data: any, more: any) => null` 不能赋值给参数类型 `(err: Error, data: any) => void`
foo((err, data, more) => null);
```

***

#### 可选的和rest参数

可选的（预先确定的）和 Rest 参数（任何数量的参数）都是兼容的：

```ts
let foo = (x: number, y: number) => {};
let bar = (x?: number, y?: number) => {};
let baz = (...args: number[]) => {};

foo = bar = baz;
baz = bar = foo;
```

> 可选的（上述例子中的 `bar`）与不可选的（上述例子中的 `foo`）仅在选项为 `strictNullChecks` 为 `false` 时兼容

***

#### 函数参数类型

双向协变（Bivariant）：旨在支持常见的事件处理方案。

```ts
// 事件等级
interface Event {
  timestamp: number;
}

interface MouseEvent extends Event {
  x: number;
  y: number;
}

interface KeyEvent extends Event {
  keyCode: number;
}

// 简单的事件监听
enum EventType {
  Mouse,
  Keyboard,
}

function addEventListener(eventType: EventType, handler: (n: Event) => void) {
  // ...
}

// 不安全，但是游泳池，常见。函数参数的比较是双向协变。
addEventListener(EventType.Mouse, (e: MouseEvent) => console.log(e.x + ',' + e.y));

// 在安全情景下的一种不好方案
addEventListener(EventType.Mouse, (e: MouseEvent) =>
  console.log((<MouseEvent>e).x + ',' + (<MouseEvent>e).y)
);
addEventListener(EventType.Mouse, <(e: Event) => void>(
  ((e: MouseEvent) => console.log(e.x + ',' + e.y))
));

// 仍然不允许明确的错误，对完全不兼容的类型会强制检查
addEventListener(EventType.Mouse, (e: number) => console.log(e));
```

同样的，你也可以把 `Array<Child>` 赋值给 `Array<Base>`（协变），因为函数是兼容的。数组的协变需要所有的函数 `Array<Child>` 都能赋值给 `Array<Base>`，例如 `push(t: Child)` 能被赋值给 `push(t: Base)`，这都可以通过函数参数双向协变实现。

下面的代码对于其他语言的开发者来说，可能会感到很困惑，因为他们认为是有错误的，可是 Typescript 并不会报错：

```ts
interface Poin2D {
  x: number;
  y: number;
}

let iTakePoint2D = (point: Point2D) => {};
let iTakePoint3D = (point: Point3D) => {};

iTakePoint3D = iTakePoint2D; // ok, 这是合理的
iTakePoint2D = iTakePoint3D; // ok，为什么？
```

***

### 枚举

枚举与数字类型相互兼容

```ts
enum Status {
  Ready,
  Waiting,
}

let status = Status.Ready;
let num = 0;

status = num;
num = status;
```

来自于不同枚举的枚举变量，被认为是不兼容的：

```ts
enum Status {
  Ready,
  Waiting,
}
enum Color {
  Red,
  Blue,
  Green,
}

let status = Status.Ready;
let color = Color.Red;

status = color; // Error
```

***

### 类

仅仅只有**实例成员和方法**会相比较，**构造函数**和**静态成员**不会被检查。

```ts
class Animal {
  feet: number;
  constructor(name: string, numFeet: number) {}
}

class Size {
  feet: number;
  constructor(meters: number) {}
}

let a: Animal;
let s: Size;

a = s; // OK
s = a; // OK
```

**私有的和受保护的成员**必须来自于相同的类。

```ts
class Animal {
  protected feet: number;
}
class Cat extends Animal {}

let animal: Animal;
let cat: Cat;

animal = cat; // ok
cat = animal; // ok

class Size {
  protected feet: number;
}

let size: Size;

animal = size; // ERROR
size = animal; // ERROR
```

***

### 泛型

TypeScript 类型系统基于变量的结构，仅当类型参数在被一个成员使用时，才会影响兼容性。如下例子中，`T` 对兼容性没有影响：

```ts
interface Empty<T> {}

let x: Empty<number>;
let y: Empty<string>;

x = y; // ok
```

当 `T` 被成员使用时，它将在实例化泛型后影响兼容性：

```ts
interface Empty<T> {
  data: T;
}

let x: Empty<number>;
let y: Empty<string>;

x = y; // Error
```

如果尚未实例化泛型参数，则在检查兼容性之前将其替换为 any：

```ts
let identity = function<T>(x: T): T {
  // ...
};

let reverse = function<U>(y: U): U {
  // ...
};

identity = reverse; // ok, 因为 `(x: any) => any` 匹配 `(y: any) => any`
```

类中的泛型兼容性与前文所提及一致：

```ts
class List<T> {
  add(val: T) {}
}

class Animal {
  name: string;
}
class Cat extends Animal {
  meow() {
    // ..
  }
}

const animals = new List<Animal>();
animals.add(new Animal()); // ok
animals.add(new Cat()); // ok

const cats = new List<Cat>();
cats.add(new Animal()); // Error
cats.add(new Cat()); // ok
```

***

## 交叉类型

交叉类型（Intersection Types）是将多个类型叠加合并组成新的类型，新类型包含了所有被合并类型的所有属性。

交叉类型的使用场景：Mixins、不适合用类来定义的场景

例如，下述代码显示了交叉类型 `Foo & Bar` 同时具备 `Foo` 和 `Bar` 两种类型的成员，就是说这个类型的对象同时拥有了这两种类型的成员。

```ts
interface Foo {
  name: string;
  age: number;
  sayName: (name: string) => void;
}

interface Bar {
  name: string;
  gender: number;
  sayGender: (gender: string) => void;
}

let Tom: Foo & Bar;

console.log(Tom.age);
console.log(Tom.gender);
```

较多在混入（Mixins）或其他不适合典型面向对象模型的地方看到交叉类型的使用。

🌰 **示例**：下面代码（[官方示例](http://www.typescriptlang.org/docs/handbook/advanced-types.html#intersection-types)）展示了如何创建一个混入的简单例子

```ts
function extend<T, U>(first: T, second: U): T & U {
  let result = <T & U>{};
  for (let prop in first) {
    (<any>result)[prop] = (<any>first)[prop];
  }
  for (let prop in second) {
    if (!(<any>result).hasOwnProperty(prop)) {
      (<any>result)[prop] = (<any>second)[prop];
    }
  }
  return result;
}

class Person {
  constructor(public name: string) {}
}
interface Loggable {
  log(): void;
}
class ConsoleLogger implements Loggable {
  log() {
    // ...
  }
}

const tom = extend(new Person('Jim'), new ConsoleLogger());
const name = tom.name;

tom.log();
```

上述代码相对比较简单，但可能对下面这段代码会产生疑问：

```ts
(<any>result)[prop] = first[prop];
```

既然 `result` 已经被断言为交叉类型，那么 `first` 所具有的属性 `result` 都是具有的。

为什么还要将 `result` 断言为 `any` 类型呢，因为交叉类型可能导致类型冲突。

🌰 **示例**：

```ts
interface Foo {
  x: boolean;
  y: string;
}

interface Bar {
  x: boolean;
  y: number;
}

type Baz = Foo & Bar;

type X = Baz['x']; // boolean
type Y = Baz['y']; // string & number

declare const baz: Baz;
declare const foo: Foo;

baz['y'] = foo['y'];
```

上面的代码中，`Foo` 和 `Bar` 接口中，`y` 属性类型冲突，那么最终 `y` 属性类型为交叉类型 `string & number`，同时 `string` 类型或者 `number` 类型无法赋值给交叉类型 `string & number`，最终导致报错。为了解决这个问题，可以将 `result` 再断言为 `any` 类型，这样 `result` 所有属性均为 `any` 类型，那么赋值就不会报错了。

现在ts会将交叉类型 `string & number`自动推断为`never`

***

## 联合类型

联合类型（Union Types）是具有或关系的多个类型组合而成，只要满足其中一个类型即可。

🌰 **示例**：

```ts
let val: string | number;
```

上述示例代码表示 `val` 值可以是 `number` 类型或者 `string` 类型的其中一种，联合类型使用 `|` 分隔每个类型。

```ts
val = true;

// index.ts(2,1): error TS2322: Type 'boolean' is not assignable to type 'string | number'.
//   Type 'boolean' is not assignable to type 'number'.
```

这里将 `val` 变量赋值为布尔值 `true`，既不是定义的 `number` 类型也不是 `string` 类型，因此会被编译为错误。

### 访问联合类型的属性和方法

# 联合类型

联合类型（Union Types）是具有或关系的多个类型组合而成，只要满足其中一个类型即可。

🌰 **示例**：

```ts
let val: string | number;
```

上述示例代码表示 `val` 值可以是 `number` 类型或者 `string` 类型的其中一种，联合类型使用 `|` 分隔每个类型。

```ts
val = true;

// index.ts(2,1): error TS2322: Type 'boolean' is not assignable to type 'string | number'.
//   Type 'boolean' is not assignable to type 'number'.
```

这里将 `val` 变量赋值为布尔值 `true`，既不是定义的 `number` 类型也不是 `string` 类型，因此会被编译为错误。

## 访问联合类型的属性或方法

当 TypeScript 不确定一个联合类型的变量到底是哪个类型的时候，我们只能访问此联合类型的所有类型里共有的属性或方法：

```ts
function getLength(val: string | number): number {
  return val.length;
}

// index.ts(2,22): error TS2339: Property 'length' does not exist on type 'string | number'.
//   Property 'length' does not exist on type 'number'.
```

上例中，`length` 不是 `string` 和 `number` 的共有属性，所以会报错。

访问 `string` 和 `number` 的共有属性（方法）是没问题的：

```ts
function getString(val: string | number): string {
  return val.toString();
}
```

联合类型的变量在被赋值的时候，会根据 [类型推论](https://tsejx.github.io/typescript-guidebook/syntax/advanced/type-inference) 的规则推断出一个类型：

```ts
let num: string | number;

num = 'seven';
console.log(num.length); // 5

num = 7;
console.log(num.length); // 编译时报错

// index.ts(5,30): error TS2339: Property 'length' does not exist on type 'number'.
```

上例中，第二行的 `num` 被推断成了 `string` 类型，访问它的 `length` 属性不会报错。

而第四行的 `num` 被推断成了 `number` 类型，访问它的 `length` 属性时就报错了。

***

## 索引类型

索引类型（Index Types）的使用让编译器能够检查使用了动态属性名的类型。

常见的 JavaScript 模式就是从对象中选取属性的子集。

🌰 **示例：**

```ts
function pluck<T, K extends keyof T>(o: T, names: K[]): T[k][] {
  return names.map(n => o[n]);
}

interface Person {
  name: string;
  age: number;
}

const tom: Person = {
  name: 'Tom',
  age: 25,
};

const values: string[] = pluck(tom, ['name']);
```

上述代码会检查 `name` 是否真的是 `Person` 的一个属性。本例还引入了几个新的类型操作符，比如 `keyof T`，索引类型的查询操作符。

### 索引查询操作符

索引类型的查询操作符 `keyof T`。

对于任何类型查询操作符，假设 `T` 是一个类型，那么 `keyof T` 产生的类型是 `T` 的属性名称字符串字面量类型构成的联合类型。

```ts
interface Person {
  name: string;
  age: number;
  address: string;
}

type person = keyof Person; // 'name' | 'age' | 'address'
```

`keyof Person` 是完全可以与 `'name' | 'age' | 'address'` 互相替换的。

不同的是如果你添加了其他的属性到 `Person`，例如 `gender: string`，那么 `keyof Person` 会**自动**变为 `'name' | 'age' | 'address' | 'gender'`。

你可以在像 `pluck` 函数这类上下文中使用 `keyof`，因为在使用之前你并不清楚可能出现的属性名。但编译器会检查你是否传入正确的属性名给 `pluck`：

```ts
pluck(tom, ['age', 'unknow']); // error: 'unknown' is not in 'name' | 'age'
```
***

### 索引访问操作符

索引访问操作符 `T[K]`，表示 `T` 的属性 `K` 的类型。

```ts
interface Person {
  name: string;
  age: number;
}

type name = Person['name'];
// type name = string
```

就像索引类型查询一样，可以在普通的上下文中使用 `T[K]`，这正是它强大所在。只要确保类型变量 `K extends keyof T` 就可以了。

***

### 字符串索引签名

如果类型 `T` 带有字符串索引签名，那么 `keyof T` 为 `string | number` 类型。

如果类型 `T` 带有数字索引签名，那么 `keyof T` 为 `number` 类型。

如果类型 `T` 带有索引签名，那么 `T[K]` 为索引签名的类型。

```ts
interface Map<T> {
  [key: string]: T;
}

let keys: keyof Map<number>;    // string

let value: Map<number>['foo'];  // number
```

***

## 映射类型

映射类型（Mapped Types）可以基于旧类型创建新类型。

常见使用场景：

- 将现有类型转换为可选的
- 将现有类型转换为只读的

在实际应用中，可能需要将现有类型转换为可选的。

🌰 **示例：**

```ts
interface Person {
  name: string;
  age: number;
  address: string;
}
```

将上述代码接口类型中的属性转换为可选。

```ts
interface PartialPerson {
  name?: string;
  age?: number;
  address?: string;
}
```

映射类型转换可以使用如下方式：

```ts
// 将原有类型所有属性转为可选的
type Partial<T> = {
  [P in keyof T]?: T[P];
};

type PartialPerson = Partial<Person>;

// 将原有类型所有属性转为只读的
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};
```

`[P in keyof T]`：类型变量 `K` 会把字符串字面量联合类型 `T` 的每个字符串都映射为属性。

当然，由于 `Partial<T>` 和 `Readonly<T>` 实用性强，它们与 `Pick` 和 `Record` 共同被包含进了 TypeScript 的标准库中。

```ts
type Pick<T, K extends keyof T> = {
  [P in K]: T[P];
};

type Record<K extends string, T> = {
  [P in K]: T;
};
```

`Readonly`，`Partial` 和 `Pick` 是同态的，但 `Record` 不是。 因为 `Record` 并不需要输入类型来拷贝属性，所以它不属于同态：

```ts
type ThreeStringProps = Record<'prop1' | 'prop2' | 'prop3', string>;
```

非同态类型本质上会创建新的属性，因此它们不会从它处拷贝属性修饰符。

***

### 其他映射类型转化案例

在真正的应用里，可能不同于上面的 Readonly 或 Partial。 它们会基于一些已存在的类型，且按照一定的方式转换字段。 这就是 `keyof` 和索引访问类型要做的事情：

```ts
type NullablePerson = {
    [P in keyof Person]: Person[P] | null,
}

type PartialPerson = {
    [P in keyof Person]?: Person[P]
}
```

但它更有用的地方是可以有一些通用的版本。

```ts
type Nullable<T> = {
  [P in keyof Person]: T[P] | null;
};

type Partial<T> = {
  [P in keyof T]?: T[P];
};
```

在这些例子中，属性列表是 `keyof T` 且结果类型是 `T[P]` 的变体。这是使用通用映射类型的一个好模版。因为这类转换是同态的，映射只作用于 `T` 的属性而没有其他的。编译器知道在添加任何新属性之前可以拷贝所以所存在的属性修饰符。例如，假设 `Person.name` 是只读的，那么 `Partial<Person>.name` 也将是只读的且为可选的。

***

### 由映射类型进行推断

现在你了解了如何包装一个类型的属性，那么接下来就是如何拆包。 其实这也非常容易：

```ts
function unproxify<T>(t: Proxify<T>): T {
  let result = {} as T;
  for (const k in t) {
    result[k] = t[k].get();
  }
  return result;
}

let originalProps = unproxify(proxyProps);
```

注意这个拆包推断只适用于**同态**的映射类型。 如果映射类型不是同态的，那么需要给拆包函数一个明确的类型参数。

***

## 条件类型

条件类型（Conditional Types）用于表达非均匀类型映射（non-uniform type mapping），能够根据类型兼容关系（即条件）从两个类型中选出一个

```ts
T extends U ? X : Y
```

语义类似于三目运算符，若 `T` 是 `U` 的自类型，则为 `X` 类型，否则就是 `Y` 类型。另外，还有一种情况是条件的真假无法确定（无法确定 `T` 是不是 `U` 的子类型），此时为 `X | Y` 类型。

🌰 **示例**：

```ts
declare function fn<T extends boolean>(x: T): T extends true ? string : number;

// x 的类型为 string | number
let x = fn(Math.random() < 0.5);
```

另外，如果 `T` 或 `U` 含有类型变量，就要等到类型变量都有对应的具体类型后才能得出条件类型的结果。

🌰 **示例**：

```ts
interface Foo {
  x: boolean;
  y: boolean;
}

declare function fn<T>(x: T): T extends Foo ? string : number;

function foo<U>(x: U) {
  // a 的类型为 U extends Foo ? string : number;
  let a = fn(x);
  let b: string | number = a;
}
```

其中 `a` 的类型为 `U extends Foo ? string : number`（即条件不确定的情况），因为 `fn(x)` 中 `x` 的类型 `U` 尚不确定，无从得知 `U` 是不是 `Foo` 的子类型。但条件类型无非两种可能类型，所以 `let b: string | number = a;` 一定是合法的（无论 `x` 是什么类型）。

***

### 嵌套条件类型

在 TypeScript 中，可以使用嵌套条件类型来创建更复杂的类型判断。以下是一个简单的例子，展示了嵌套条件类型的用法：

```ts
typescriptCopy codetype MyType<T> = T extends string
  ? {
      isString: true;
      value: string;
    }
  : T extends number
  ? {
      isNumber: true;
      value: number;
    }
  : {
      isOther: true;
      value: T;
    };

// 使用示例
const strResult: MyType<string> = {
  isString: true,
  value: "Hello, TypeScript!",
};

const numResult: MyType<number> = {
  isNumber: true,
  value: 42,
};

const otherResult: MyType<boolean> = {
  isOther: true,
  value: true,
};
```

在这个例子中，我们定义了一个泛型类型 `MyType<T>`，它根据 `T` 的类型进行条件判断，返回不同的结构。如果 `T` 是 `string`，则返回包含 `isString` 和 `value` 的对象；如果 `T` 是 `number`，则返回包含 `isNumber` 和 `value` 的对象；否则，返回包含 `isOther` 和 `value` 的对象。

这种嵌套条件类型的使用方式可以根据实际需要进行扩展，以适应更复杂的类型判断场景。在实际开发中，这种技术常用于创建通用的、灵活的类型工具。

***

### 可分配条件类型









***

## 关键字

| 关键字       | 功能与介绍                                     | 用法示例                                                     |
| ------------ | ---------------------------------------------- | ------------------------------------------------------------ |
| `type`       | 创建类型别名，提高代码可读性和可维护性         | `type Point = { x: number; y: number; };`                    |
| `interface`  | 声明对象的结构，用于类的契约或描述对象的形状   | `interface Person { name: string; age: number; }`            |
| `enum`       | 定义枚举类型，提高代码可读性                   | `enum Color { Red, Green, Blue };`                           |
| `namespace`  | 创建命名空间，避免全局命名冲突                 | `namespace Geometry { export class Circle { /* ... */ } }`   |
| `abstract`   | 声明抽象类或抽象方法                           | `abstract class Shape { abstract calculateArea(): number; }` |
| `super`      | 在派生类中调用父类的方法                       | `class Dog extends Animal { makeSound() { super.makeSound(); /* ... */ } }` |
| `readonly`   | 创建只读属性，一旦赋值后不能再被修改           | `class Person { readonly name: string; /* ... */ }`          |
| `implements` | 在类中实现接口，确保类满足接口定义的规范       | `class Circle implements Shape { /* ... */ }`                |
| `extends`    | 在类之间建立继承关系，子类继承父类的属性和方法 | `class Dog extends Animal { /* ... */ }`                     |
| `export`     | 导出模块中的变量、函数、类等                   | `export class MyClass { /* ... */ }`                         |
| `import`     | 导入模块中的变量、函数、类等                   | `import { MyClass } from './myModule';`                      |
| `public`     | 指定类的属性或方法可以在类的外部访问           | `class MyClass { public myProperty: string; }`               |
| `private`    | 将类的属性或方法限制在类的内部访问             | `class MyClass { private myProperty: string; }`              |
| `protected`  | 允许类的属性或方法在类的派生类中访问           | `class MyClass { protected myProperty: string; }`            |
