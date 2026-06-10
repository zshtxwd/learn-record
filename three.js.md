## THREE.js

### 场景

#### 创建场景

### 形状

#### 创建形状

### 材质

#### 创建材质

### 模型

#### 添加模型

#### 修改模型位置

### 相机

#### 添加相机

##### 修改相机位置

##### 设置相机拍摄目标

### 渲染器

#### 创建渲染器

#### 设置canvas画布尺寸

### 坐标系

#### 添加坐标系

### 光源

#### 光源对不同材质的影响

##### 基础材质

基础材质不受影响

##### 漫反射材质



#### THREE光源的种类

##### 环境光AmbientLight

```javascript
// 创建环境光
// 第一个参数是光的颜色
// 第二个参数是光的强度
const ambientlight = new THREE.AmbientLight(0xFFFF00,0.5)

// 将环境光添加到场景中
scene.add(ambientlight)
```

**点光源可视化**

```javascript
// 可视化点光源
const pointlighthelper=new THREE.PointLightHelper(pointlight,20)
// 第一个参数是要可视化的是那个点光源
// 可视化的点光源大小

// 将可视化的点光源加入到场景中
scene.add(pointlighthelper)
```



##### 点光源PointLight

##### 聚光灯光源SpotLight

##### 平行光DirectionalLight

```javascript
// 创建平行光
// 第一个参数是光的颜色
// 第二个参数是光的强度
const directionallight=new THREE.DirectionalLight(0xffffff,1)

// 设置平行光的位置(其实是平行光的起点)
directionallight.position.set(400, 200, 100)

// 设置平行光照射的目标(平行光的终点，他和起点构成一条线，从而确定平行光的方向)
directionallight.target=mesh

// 将平行光加入场景中
scene.add(directionallight)
```

**平行光可视化**

```javascript
// 平行光可视化
// 第一个参数是要可视化的是那个平行光
// 第二个参数可视化的平行光大小
// 第三个参数可视化的平行光的颜色
const directionallighthelper=new THREE.DirectionalLightHelper(directionallight,20,0xff0000)

// 将可视化的平行光放到场景中
scene.add(directionallighthelper)
```

#### 添加光源

```javascript
// 创建点光源
const pointlight = new THREE.PointLight(0xffffff, 1.0) 
//第一个参数是光照颜色，第二个参数是光照强度

// 设置点光源的位置
pointlight.position.set(400, 200, 100)

// 将点光源放置到场景中
scene.add(pointlight)
```



### 相机控件OrbitControls

通过相机控件OrbitControls实现旋转缩放拖动等预览效果

```javascript
// 创建相机轨道控制器控件对象
const controls=new OrbitControls(camera, renderer.domElement)
// 缩放，旋转，移动本质上是改变了相机的位置
// 第一个参数，我要改变位置的那个相机
// 第二个参数，我要监控的区域

// 使用事件监听器监听控制器变化，从而重新渲染
controls.addEventListener("change",()=>{
	renderer.render(scene, camera)
})
```

### Gui

### FPS

### 几何体顶点位置数据和点模型

```javascript
//创建一个空的几何体对象
const geometry = new THREE.BufferGeometry(); 
```

#### `BufferAttribute`定义几何体顶点数据

使用JavaScript的类型化数组Float32Array创建一组xyz坐标数据用来表示几何体的顶点坐标

Float32Array只能保存4字节浮点数，接收一个参数限制长度，或者其他数组，会将非数字类型的元素变为NaN

```javascript
//类型化数组创建顶点数据
const vertices = new Float32Array([
    0, 0, 0, //顶点1坐标
    50, 0, 0, //顶点2坐标
    0, 100, 0, //顶点3坐标
    0, 0, 10, //顶点4坐标
    0, 0, 100, //顶点5坐标
    50, 0, 10, //顶点6坐标
]);
```

通过threejs的属性缓冲区对象BufferAttribute表示threejs几何体顶点数据\

```javascript
// 创建属性缓冲区对象
//3个为一组，表示一个顶点的xyz坐标
const attribue = new THREE.BufferAttribute(vertices, 3); 
```

#### 设置几何体顶点`.attributes.position`

通过`geometry.attributes.position`设置几何体顶点位置属性的值`BufferAttribute`。

```javascript
// 设置几何体attributes属性的位置属性
geometry.attributes.position = attribue;
```

### 点模型`Points`

点模型Points 和网格模型`Mesh`一样，都是threejs的一种模型对象，只是大部分情况下都是用Mesh表示物体。

网格模型`Mesh`有自己对应的网格材质，同样点模型`Points`有自己对应的点材质PointsMaterial

```javascript
// 点渲染模式
const material = new THREE.PointsMaterial({
    color: 0xffff00,
    size: 10.0 //点对象像素尺寸
}); 
```

几何体geometry作为点模型Points参数，会把几何体渲染为点，把几何体作为Mesh的参数会把几何体渲染为面。

```javascript
const points = new THREE.Points(geometry, material); //点模型对象
```



### 线模型对象

#### 线模型`Line`渲染顶点数据

下面代码是把几何体作为线模型Line 的参数，你会发现渲染效果是从第一个点开始到最后一个点，依次连成线。

```javascript
// 线材质对象
const material = new THREE.LineBasicMaterial({
    color: 0xff0000 //线条颜色
}); 
// 创建线模型对象
const line = new THREE.Line(geometry, material);
```

#### 线模型`LineLoop`、`LineSegments`

threejs线模型除了Line，还提供了LineLoop、LineSegments ，区别在于绘制线条的规则不同。

```javascript
// 闭合线条
const line = new THREE.LineLoop(geometry, material); 
//非连续的线条
const line = new THREE.LineSegments(geometry, material);
```

### 网格模型

三个点可以表示一个面，three.js使用三角形来构成几何体

三角形有正反两面之分，如果构成三角形的三个点呈逆时针排列就是正面，如果顺时针排列就是反面，默认情况反面是不可见的

### 双面可见

Three.js的材质默认正面可见，反面不可见。

```javascript
const material = new THREE.MeshBasicMaterial({
    color: 0x0000ff, //材质颜色
    side: THREE.FrontSide, //默认只有正面可见
});
const material = new THREE.MeshBasicMaterial({
    side: THREE.DoubleSide, //两面可见
});
const material = new THREE.MeshBasicMaterial({
    side: THREE.BackSide, //设置只有背面可见
});
```

### 几何体顶点索引数据       

网格模型Mesh对应的几何体BufferGeometry，拆分为多个三角后，很多三角形重合的顶点位置坐标是相同的，这时候如果你想减少顶点坐标数据量，可以借助几何体顶点索引`geometry.index`来实现。

### 定义顶点位置坐标数据

每个三角形3个顶点坐标，矩形平面可以拆分为两个三角形，也就是6个顶点坐标。

```javascript
const vertices = new Float32Array([
    0, 0, 0, //顶点1坐标
    80, 0, 0, //顶点2坐标
    80, 80, 0, //顶点3坐标
    0, 0, 0, //顶点4坐标   和顶点1位置相同
    80, 80, 0, //顶点5坐标  和顶点3位置相同
    0, 80, 0, //顶点6坐标
]);
```

如果几何体有顶点索引`geometry.index`，那么你可以吧三角形重复的顶点位置坐标删除。

```javascript
const vertices = new Float32Array([
    0, 0, 0, //顶点1坐标
    80, 0, 0, //顶点2坐标
    80, 80, 0, //顶点3坐标
    0, 80, 0, //顶点4坐标
]);
```

![顶点索引](http://www.webgl3d.cn/threejs/%E9%A1%B6%E7%82%B9%E7%B4%A2%E5%BC%95.jpg)

### `BufferAttribute`定义顶点索引`.index`数据

通过javascript类型化数组`Uint16Array`创建顶点索引`.index`数据。

```javascript
// Uint16Array类型数组创建顶点索引数据
const indexes = new Uint16Array([
    // 下面索引值对应顶点位置数据中的顶点坐标
    0, 1, 2, 0, 2, 3,
])
```

通过threejs的属性缓冲区对象BufferAttribute表示几何体顶点索引`.index`数据。

```javascript
// 索引数据赋值给几何体的index属性
geometry.index = new THREE.BufferAttribute(indexes, 1); //1个为一组
```

 ### 顶点法线数据

`MeshBasicMaterial`材质改为`MeshLambertMaterial`材质不能正常显示，因为使用受光照影响的材质，几何体BufferGeometry需要定义**顶点法线**数据

```javascript
// MeshBasicMaterial不受光照影响
// 使用受光照影响的材质，几何体Geometry需要定义顶点法线数据
const material = new THREE.MeshLambertMaterial({
    color: 0x0000ff, 
    side: THREE.DoubleSide, //两面可见
});
```

### 矩形平面几何体法线案例——无顶点索引

Three.js中法线是通过顶点定义，默认情况下，每个顶点都有一个法线数据，就像每一个顶点都有一个位置数据。

因为向量是两个点计算出来的，所以只用设置一个点数据

```js
// 矩形平面，无索引，两个三角形，6个顶点
// 每个顶点的法线数据和顶点位置数据一一对应
const normals = new Float32Array([
    0, 0, 1, //顶点1法线( 法向量 )
    0, 0, 1, //顶点2法线
    0, 0, 1, //顶点3法线
    0, 0, 1, //顶点4法线
    0, 0, 1, //顶点5法线
    0, 0, 1, //顶点6法线
]);
// 设置几何体的顶点法线属性.attributes.normal
geometry.attributes.normal = new THREE.BufferAttribute(normals, 3); 
```

### 矩形平面几何体法线案例——有顶点索引

```js
// 矩形平面，有索引，两个三角形，有2个顶点重合，有4个顶点
// 每个顶点的法线数据和顶点位置数据一一对应
const normals = new Float32Array([
    0, 0, 1, //顶点1法线( 法向量 )
    0, 0, 1, //顶点2法线
    0, 0, 1, //顶点3法线
    0, 0, 1, //顶点4法线
]);
// 设置几何体的顶点法线属性.attributes.normal
geometry.attributes.normal = new THREE.BufferAttribute(normals, 3);
```

### three.js自带的几何体顶点

### 查看几何体顶点位置和索引数据

可以用顶点索引index数据构建几何体，也可以不用，threejs默认的大部分几何体都有三角形的顶点索引数据，具体可以通过浏览器控制台打印几何体数据查看。

```js
const geometry = new THREE.PlaneGeometry(100,50); //矩形平面几何体
// const geometry = new THREE.BoxGeometry(50,50,50); //长方体

console.log('几何体',geometry);
console.log('顶点位置数据',geometry.attributes.position);
console.log('顶点索引数据',geometry.index);
```

### 材质属性`.wireframe`

线条模式渲染，查看几何体三角形结构

```js
const material = new THREE.MeshLambertMaterial({
    color: 0x00ffff, 
    wireframe:true,//线条模式渲染mesh对应的三角形数据
});
```

### 几何体细分数

Three.js很多几何体都提供了**细分数**相关的参数，这里以矩形平面几何体`PlaneGeometry`为例介绍。

矩形平面几何体至少需要两个三角形拼接而成。

```js
 //矩形几何体PlaneGeometry的参数3,4表示细分数，默认是1,1
const geometry = new THREE.PlaneGeometry(100,50,1,1);
```

把一个矩形分为2份，每个矩形2个三角形，总共就是4个三角形

```js
const geometry = new THREE.PlaneGeometry(100,50,2,1);
```

把一个矩形分为4份，每个矩形2个三角形，总共就是8个三角形

```js
const geometry = new THREE.PlaneGeometry(100,50,2,2);
```

### 球体`SphereGeometry`细分数

球体`SphereGeometry`参数2、3分别代表宽、高度两个方向上的细分数，默认32,16，具体多少以你所用版本为准。

```js
const geometry = new THREE.SphereGeometry( 50, 32, 16 );
```

如果球体细分数比较低，表面就不会那么光滑。

```js
const geometry = new THREE.SphereGeometry( 15, 8, 8 );
```

### 三角形数量与性能

对于一个曲面而言，细分数越大，表面越光滑，但是三角形和顶点数量却越多。

几何体三角形数量或者说顶点数量直接影响Three.js的渲染性能，在不影响渲染效果的情况下，一般尽量越少越好。

###  旋转、缩放、平移几何体

BufferGeometry通过`.scale()`、`.translate()`、`.rotateX()`、`.rotateY()`等方法可以对几何体本身进行缩放、平移、旋转,这些方法本质上都是改变几何体的顶点数据。

![img](http://www.webgl3d.cn/imgthreejs/BufferGeometry.svg)

```js
// 几何体xyz三个方向都放大2倍
geometry.scale(2, 2, 2);
// 几何体沿着x轴平移50
geometry.translate(50, 0, 0);
// 几何体绕着x轴旋转45度
geometry.rotateX(Math.PI / 4);
// 几何体旋转、缩放或平移之后，查看几何体顶点位置坐标的变化
// BufferGeometry的旋转、缩放、平移等方法本质上就是改变顶点的位置坐标
console.log('顶点位置数据', geometry.attributes.position);
```

### 缩放`.scale()`

```js
// 几何体xyz三个方向都放大2倍
geometry.scale(2, 2, 2);

// 几何体旋转、缩放或平移之后，查看几何体顶点位置坐标的变化
// BufferGeometry的旋转、缩放、平移等方法本质上就是改变顶点的位置坐标
console.log('顶点位置数据', geometry.attributes.position);
```

### 平移`.translate()`

```js
// 几何体沿着x轴平移50
geometry.translate(50, 0, 0);
```

### 旋转`.rotateX()`、`.rotateY()`、`.rotateZ()`

```js
// 几何体绕着x轴旋转45度
geometry.rotateX(Math.PI / 4);
```

### 居中`.center()`

```js
geometry.translate(50, 0, 0);//偏移
// 居中：已经偏移的几何体居中，执行.center()，你可以看到几何体重新与坐标原点重合
geometry.center();
```
