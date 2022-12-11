import React, { useState } from "react"
import "./Expenses.css"
import ExpenseItem from "./ExpenseItem"
import Card from "../UI/Card.js"
import ExpensesFilter from "./ExpenseFilter"

function Expenses(props) {
  const expenses = props.data
  const [yearData, setYearData] = useState("2022")
  const [nExp, setNExp] = useState(props.data)
  function filterByYear(y) {
    setYearData(y)
    setNExp(
      expenses.filter((val) => {
        console.log(val.date.getFullYear())
        console.log(typeof val.date.getFullYear())
        console.log(y, typeof y, "y")
        return val.date.getFullYear() === parseInt(y)
      })
    )
    console.log(expenses)
  }

  return (
    <Card className="expenses">
      <ExpensesFilter onGetYear={filterByYear} selected={yearData} />
      {nExp.map((val, idx) => {
        return (
          <div>
            <ExpenseItem data={val} key={`expense-item-${idx}`} />
          </div>
        )
      })}
    </Card>
  )
}

export default Expenses
