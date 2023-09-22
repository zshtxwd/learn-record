# Pinia

#### 安装

```
npm install pinia
```

#### 配置

创建store文件夹

创建index文件

```javascript
import { createPinia } from 'pinia'

let pinia = createPinia()

export default pinia
```

#### 引入

```javascript
import pinia from './store'

app.use(pinia)
```

#### 创建

创建module文件

创建小仓库文件，例如用户相关信息的仓库user.ts

```javascript
import {defineStore} from pinia

let useUserStore = defineStore("User",{
    //仓库存储数据的地方
    state:()=>{
        return {
            
        }
    },
    //异步|逻辑的地方
    actions:{},
    getters:{}
})

//对外暴露小仓库
export default useUserStore
```

#### 使用

##### 引入

在需要使用小仓库的vue文件中，引入小仓库

```javascript
import useUserStore from "@/store/module/user.ts"

let useStore = useUserStore()

之后就可以调用我们之前定义好的方法
```



