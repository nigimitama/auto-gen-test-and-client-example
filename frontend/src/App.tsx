import "./App.css"
import { rootGet } from "./client"
import { useEffect, useState } from "react"

function App() {
  const [value, setValue] = useState<string | undefined>()
  useEffect(() => {
    rootGet().then(({ data }) => {
      setValue(data)
    })
  }, [])

  return (
    <>
      <h1>{value}</h1>
    </>
  )
}

export default App
