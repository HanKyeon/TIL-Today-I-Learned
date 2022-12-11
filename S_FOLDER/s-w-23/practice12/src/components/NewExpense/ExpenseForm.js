import "./ExpenseForm.css"
import React, { useState } from "react"

function ExpenseForm(props) {
  // const [inputData, setInputData] = useState({
  //   title: "",
  //   amount: 0,
  //   date: "",
  // })
  const [inputTitle, setInputTitle] = useState("")
  const [inputAmount, setInputAmount] = useState(0)
  const [inputDate, setInputDate] = useState("2022-12-01")
  function titleChangeHandler(event) {
    event.preventDefault()
    setInputTitle(event.target.value)
    // setInputData({
    //   ...inputData,
    //   title: event.target.value,
    // })
    // setInputData((prevState) => {
    //   return { ...prevState, inputTitle: event.target.value }
    // })
  }
  function amountChangeHandler(event) {
    event.preventDefault()
    setInputAmount(event.target.value)
    // setInputData({
    //   ...inputData,
    //   amount: event.target.value,
    // })
    // setInputData((prevState) => {
    //   return { ...prevState, inputAmount: event.target.value }
    // })
  }
  function dateChangeHandler(event) {
    event.preventDefault()
    setInputDate(event.target.value)
    // setInputData({
    //   ...inputData,
    //   date: event.target.value,
    // })
    // setInputData((prevState) => {
    //   return { ...prevState, inputDate: event.target.value }
    // })
  }
  function submitHandler(event) {
    event.preventDefault()
    const expenseData = {
      title: inputTitle,
      amount: inputAmount,
      date: new Date(inputDate),
    }
    setInputTitle("")
    setInputAmount(0)
    setInputDate("")
    props.onSaveExpenseData(expenseData)
  }
  return (
    <form onSubmit={submitHandler}>
      <div className="new-expense__controls">
        <div className="new-expense__control">
          <label>Title</label>
          <input
            type="text"
            onChange={titleChangeHandler}
            value={inputTitle}
            placeholder="데이터 입력"
          />
        </div>
        <div className="new-expense__control">
          <label>Amount</label>
          <input
            type="number"
            min="0.01"
            step="0.01"
            onChange={amountChangeHandler}
            value={inputAmount}
          />
        </div>
        <div className="new-expense__control">
          <label>Date</label>
          <input
            type="date"
            min="2019-01-01"
            max="2024-12-31"
            onChange={dateChangeHandler}
            value={inputDate}
          />
        </div>
      </div>
      <div className="new-expense__actions">
        <button type="submit">Add Expense</button>
      </div>
    </form>
  )
}

export default ExpenseForm
