import "./ExpenseDate.css"

function ExpenseDate(props) {
  return (
    <div className="expense-item">
      <div>{props.data.month}</div>
      <div>{props.data.year}</div>
      <div>{props.data.day}</div>
    </div>
  )
}

export default ExpenseDate
