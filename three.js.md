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

