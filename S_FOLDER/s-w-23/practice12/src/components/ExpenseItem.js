import ExpenseDate from "./ExpenseDate"
import "./ExpenseItem.css"

function ExpenseItem(props) {
  const dateData = {
    date: props.data.date,
  }
  return (
    <div className="expense-item">
      <ExpenseDate data={dateData} />
      <div className="expense-item__description">
        <h2>{props.data.title}</h2>
        <div className="expense-item__price">${props.data.amount}</div>
      </div>
    </div>
  )
}

export default ExpenseItem
