import "./NewExpense.css"
import React from "react"
import Card from "../UI/Card"
import ExpenseForm from "./ExpenseForm"

function NewExpense(props) {
  const onSaveExpenseDataHandler = (enteredExpenseData) => {
    const expenseData = {
      ...enteredExpenseData,
      id: Math.random().toString(),
    }
    props.addExpenseHandler(expenseData)
  }
  return (
    <Card className="new-expense">
      <ExpenseForm onSaveExpenseData={onSaveExpenseDataHandler} />
    </Card>
  )
}

export default NewExpense
