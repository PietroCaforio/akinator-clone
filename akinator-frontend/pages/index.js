import { useEffect, useState } from "react";
import axios from "axios";
import { v4 as uuidv4 } from "uuid";

export default function Home() {
  const [sessionId, setSessionId] = useState("");
  const [question, setQuestion] = useState(null);
  const [guess, setGuess] = useState(null);
  const [loading, setLoading] = useState(false);

  // Start a new game on mount
  useEffect(() => {
    const newSession = uuidv4();
    setSessionId(newSession);
    axios.get(`http://localhost:8000/start_game?session_id=${newSession}`)
      .then(res => setQuestion(res.data.question))
      .catch(err => console.error(err));
  }, []);

  const handleAnswer = async (answer) => {
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/answer", {
        session_id: sessionId,
        answer_yes: answer
      });

      if (res.data.question) {
        setQuestion(res.data.question);
      } else if (res.data.guess) {
        setGuess(res.data.guess);
        setQuestion(null);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const restartGame = () => {
    window.location.reload(); // simple way to reset everything
  };

  return (
    <main style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Akinator Clone 🤖</h1>

      {question && (
        <>
          <h2>Question:</h2>
          <p>Is the answer to <strong>{question}</strong> yes?</p>
          <button disabled={loading} onClick={() => handleAnswer(true)}>Yes</button>
          <button disabled={loading} onClick={() => handleAnswer(false)}>No</button>
        </>
      )}

      {guess && (
        <>
          <h2>🧠 My guess is:</h2>
          <h3>{guess}</h3>
          <button onClick={restartGame}>Play Again</button>
        </>
      )}

      {!question && !guess && (
        <p>Loading...</p>
      )}
    </main>
  );
}
