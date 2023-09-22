#### echarts-liquidfill option示例
```javascript
{
    data: [], // 数据数组，通常包含液体填充的值

    color: ['#294D99', '#156ACF', '#1598ED', '#45BDFF'], // 液体填充的颜色，可以是一个颜色数组
    
    center: ['50%', '50%'], // 液体填充的中心位置，通常设置为 '50%' 表示居中
    
    radius: '50%', // 液体填充的半径，通常设置为 '50%' 表示半径与容器大小相同
    
    amplitude: '8%', // 波浪振幅，控制波浪的高度
    
    waveLength: '80%', // 波浪长度，控制波浪的宽度
    
    phase: 'auto', // 波浪相位，通常设置为 'auto'
    
    period: 'auto', // 波浪周期，通常设置为 'auto'
    
    direction: 'right', // 波浪方向，可以是 'right' 或 'left'
    
    shape: 'circle', // 液体填充的形状，可以是 'circle'（圆形）等
    
    waveAnimation: true, // 是否开启波浪动画
    
    animationEasing: 'linear', // 波浪动画的缓动函数
    
    animationEasingUpdate: 'linear', // 更新动画的缓动函数
    
    animationDuration: 2000, // 波浪动画的持续时间，以毫秒为单位
    
    animationDurationUpdate: 1000, // 更新动画的持续时间，以毫秒为单位
    
    outline: {
        show: true, // 是否显示外边框
    
        borderDistance: 8, // 外边框与液体填充之间的距离
    
        itemStyle: {
            color: 'none', // 外边框的颜色
            borderColor: '#294D99', // 外边框的边框颜色
            borderWidth: 8, // 外边框的边框宽度
            shadowBlur: 20, // 外边框的阴影模糊大小
            shadowColor: 'rgba(0, 0, 0, 0.25)' // 外边框的阴影颜色
        }
    },
    
    backgroundStyle: {
        color: '#E3F7FF' // 背景颜色
    },
    
    itemStyle: {
        opacity: 0.95, // 液体填充的透明度
        shadowBlur: 50, // 液体填充的阴影模糊大小
        shadowColor: 'rgba(0, 0, 0, 0.4)' // 液体填充的阴影颜色
    },
    
    label: {
        show: true, // 是否显示标签
    
        color: '#294D99', // 标签的文字颜色
        insideColor: '#fff', // 标签的内部文字颜色
        fontSize: 50, // 标签的文字大小
        fontWeight: 'bold', // 标签的文字粗细
    
        align: 'center', // 标签文字的水平对齐方式
        baseline: 'middle', // 标签文字的垂直对齐方式
        position: 'inside' // 标签的位置，通常设置为 'inside' 表示在液体填充内部
    },
    
    emphasis: {
        itemStyle: {
            opacity: 0.8 // 高亮状态下液体填充的透明度
        }
    }
}
```