import ExpenseDate from "./ExpenseDate"
import "./ExpenseItem.css"

function ExpenseItem(props) {
  const month = props.expItem.date.toLocaleString("en-US", { month: "long" })
  const year = props.expItem.date.getFullYear()
  const day = props.expItem.date.toLocaleString("en-US", { day: "2-digit" })
  const dateData = {
    month,
    year,
    day,
  }
  return (
    <div className="expense-item">
      <ExpenseDate data={dateData} />
      <div className="expense-item__description">
        <h2>{props.expItem.title}</h2>
        <div className="expense-item__price">${props.expItem.amount}</div>
      </div>
    </div>
  )
}

export default ExpenseItem
