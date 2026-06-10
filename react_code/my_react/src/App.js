// 项目根组件
// App => index.js = >index.html(div#root)

import { useState } from 'react'

function Button () {
  const [i,setI]=useState(0)

  const handleClick = ()=>{
    setI(preI=>preI+1)
  }
  return (
    <button onClick={handleClick}>click me:{i}</button>
  )
}

function App() {
  return (
    <div className="App">
      <Button/>
    </div>
  );
}

export default App;