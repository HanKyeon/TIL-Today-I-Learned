import "./ExpenseDate.css"
import Card from "../UI/Card.js"

function ExpenseDate(props) {
  const month = props.data.date.toLocaleString("en-US", { month: "long" })
  const year = props.data.date.getFullYear()
  const day = props.data.date.toLocaleString("en-US", { day: "2-digit" })
  return (
    <Card className="expense-date">
      <div className="expense-date__month">{month}</div>
      <div className="expense-date__year">{year}</div>
      <div className="expense-date__day">{day}</div>
    </Card>
  )
}

export default ExpenseDate
