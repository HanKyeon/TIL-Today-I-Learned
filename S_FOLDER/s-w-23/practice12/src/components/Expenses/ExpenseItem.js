import React, { useState } from "react"
import ExpenseDate from "./ExpenseDate"
import "./ExpenseItem.css"

function ExpenseItem(props) {
  const [title, changeTitle] = useState(props.data.title)
  const dateData = {
    date: props.data.date,
  }
  function foo(event) {
    event.preventDefault()
    changeTitle("Updated!")
  }
  return (
    <div className="expense-item" key={props.key}>
      <ExpenseDate data={dateData} />
      <div className="expense-item__description">
        <h2>{props.data.title}</h2>
        <div className="expense-item__price">${props.data.amount}</div>
      </div>
      <button onClick={foo}>Change Title</button>
    </div>
  )
}

export default ExpenseItem
