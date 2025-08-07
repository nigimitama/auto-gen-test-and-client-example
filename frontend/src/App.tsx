import "./App.css"
import { useQuery } from "./lib/api/client"

function App() {
  return (
    <>
      <h1>Sample App</h1>

      <Greeting />
    </>
  )
}

function Greeting() {
  const { data, error, isLoading, isValidating, mutate } = useQuery("/")
  console.log({ data, error, isLoading, isValidating, mutate })

  if (isLoading) {
    return <p>読み込み中...</p>
  }

  if (error) {
    return <p>エラーが発生しました: {error.message}</p>
  }

  return <p>{data}</p>
}

export default App
