import { useState } from 'react'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Desktop from "./pages/Desktop";
import Login from "./pages/Login"
import './App.css'

const router = createBrowserRouter([
  {path: "/", element: <Desktop/>},
  {path: "/login", element: <Login/>}
])

function App() {

  return (
    <RouterProvider router = {router}/>
  )
}

export default App
