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
			<Header />	{/* It is more appropriate i think to make header and footer objects, and pass items needed in such as location bar and navbar - think semantically does it make sense for the location bar to be ap art of the header? no? but placewise does it? ?? */}
			<NavBar />
			<Routes>
				<Route path="/" element={<HomePage />} />
				<Route path="/map" element={<h1>Not Found</h1>} />
				<Route path="/list" element={<h1>Not </h1>} />
				<Route path="/settings" element={<h1> Found</h1>} />
			</Routes>
		</Router>
	</ErrorProvider>
	</>
  )
}

export default App
