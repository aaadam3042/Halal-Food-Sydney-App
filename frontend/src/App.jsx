import './App.css'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ErrorProvider } from '@contexts/ErrorContext'
import { ErrorPopup } from '@components/ErrorPopup'
import { Header } from '@components/Header'
import { HomePage } from '@pages/user/HomePage'
import NavBar from '@components/NavBar';

function App() {
	return (
	<>
	<ErrorProvider>
		<ErrorPopup />
		<Router>
			<Header />
			<Routes>
				<Route path="/" element={<HomePage />} />
				<Route path="/map" element={<h1>Not Found</h1>} />
				<Route path="/list" element={<h1>Not </h1>} />
				<Route path="/settings" element={<h1> Found</h1>} />
			</Routes>
			<NavBar />
		</Router>
	</ErrorProvider>
	</>
  )
}

export default App
