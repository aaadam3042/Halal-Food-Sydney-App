import LocationSearchBar from '@components/LocationSearchBar';
import { ServiceCard } from '@components/ServiceCard';
import Page from '@components/Page';
import {Header} from '@components/Header'
import { Box } from '@mui/material';

let restaurantServices = [
	{id:1, name: 'mine', distance: '1km', openTime:'1-2pm', contact: '0480', halalStatus: 'HALAL'}, 
	{id:2, name: 'mine1', distance: '1km', openTime:'1-2pm', contact: '0480', halalStatus: 'HALAL'},
	{id:3, name: 'mine2', distance: '1km', contact: '0480', halalStatus: 'HALAL'},
]

export function HomePage() {

  	return (
	<>	
		<LocationSearchBar />
		<h1>Home Page</h1>
		<p>This is the home page</p>
		<ServiceCard title="Restaurants" services={restaurantServices} />
		<ServiceCard title="Butchers" services={restaurantServices} />
	</>
  	);
}

export default HomePage;