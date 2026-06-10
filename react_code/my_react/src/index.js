// index.js是整个项目的入口，项目从这里开始运行

// 导入react必要的两个核心包
import React from 'react'
import ReactDOM from 'react-dom/client'

// 导入项目的根组件
import App from './App'

// 把App根组件渲染到一个id为root的dom节点上
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
    <App />
)

