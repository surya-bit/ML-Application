import { useState, useEffect } from 'react'

import axios from 'axios'
import Chart from 'chart.js/auto'
import { Line } from 'react-chartjs-2';

import { getRelativePosition } from 'chart.js/helpers';
import './App.css'
import DropdownMenu from './components/DropdownMenu'

function App() {
  const [results, setResults] = useState({
    monthValue:null ,
    monthData:[1,2,3,4],
    yearData:[1,2,3,4]
  })
    /*{
    valuesformonth: [1,2,3,4,5],
    valuesforyear: [200, 300,344, 566]
  })*/
  
  const monthLabels = Array.from({length: results.monthData[0].length}, (_, i) => i + 1)
  const yearLabels = Array.from({length: results.yearData[0].length}, (_, i) => i + 1)
  
  const [selectedOption, setSelectedOption] = useState(null);
  const yearData = {
    labels: results !== null ? yearLabels : [1,2,3,4],
    datasets: [
      {
        label: 'Prediction for the year',
        data: results !== null ? results.yearData[0] : [1,2,3,4],
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.4)',
      },
    ],
  };
  const MonthData = {
    labels: results !== null ? monthLabels : [1,2,3,4],
    datasets: [
      {
        label: 'Prediction for the month',
        data: results !== null ? results.monthData[0] : [1,2,3,4],
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.4)',
      },
    ],
  };

  const options = {
    scales: {
      y: {
        beginAtZero: false,
      },
      x:{
        interval: 12
      },
    },
  };

  const postData = {
    key1: selectedOption,
    
  }
  //localhost server link to server.py
  const apiUrl = 'http://127.0.0.1:5000'
  useEffect(() => {
    const delayTimer = setTimeout(() => {
      // Make a request to your search endpoint when the user stops typing
      if (selectedOption.trim() !== '') {

     axios.post(apiUrl,postData).then((response) => setResults(response.data)).catch((error) => console.error(error) )
          
      }
    }, 500); // Adjust the delay (in milliseconds) as needed

    // Cleanup the timer on component unmount or when the query changes
    return () => clearTimeout(delayTimer);
  }, [selectedOption]);

  
  
   
  
   
  return (
    <div className='flex flex-col items-center  h-screen w-screen'>
      <div className='flex w-full justify-between items-center'>
        <span className='font-black text-6xl italic p-10'>Fetch Client</span>
        <span className='text-slate-700 mr-3'>built by Suryaraj Machani</span>
      </div>
      <div className='mt-[50px]' >
      
      <DropdownMenu selectedOption={selectedOption} setSelectedOption={setSelectedOption} />
      
      </div>
{
  results != null  ?  
  <div className='font-black text-2xl'>
  <span>Predicted value for this month is </span>
    {results.monthValue}
    {console.log(monthLabels)}
    
    <div className='flex flex-col mt-9 w-screen'>
    
    <Line data={MonthData} options={options} />
    <Line data={yearData}  options={options}  />
    
    </div>
  </div>
  :
  null

}
    </div>
  )
}

export default App
