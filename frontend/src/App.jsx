import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='flex h-screen w-full items-center justify-center'>
        <h1 className='font-medium text-amber-400'>Hi, this is travelperk</h1>
      </div>
    </>
  )
}

export default App
