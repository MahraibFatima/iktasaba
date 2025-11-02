import './App.css'
import { faqData } from './data.js'
function App() {
  return (
    <>
      {
        faqData.map(item => (
          <div key={item.id}>
            <h2>{item.question}</h2>
            <p>{item.answer}</p>
          </div>
        ))}

      <h1>Hi React!</h1>
    </>
  )
}

export default App