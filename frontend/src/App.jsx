import './App.css'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ErrorProvider } from '@contexts/ErrorContext'
import { ErrorPopup } from '@components/ErrorPopup'
import { HomePage } from '@pages/user/HomePage'
import NavBar from '@components/NavBar';

function App() {
	return (
	<>
	<ErrorProvider>
		<ErrorPopup />
		  <Router>
			<Routes>
				<Route path="/" element={<HomePage />} />
			</Routes>
		  </Router>
		  <NavBar />
	</ErrorProvider>
	</>
  )
}

export default App
