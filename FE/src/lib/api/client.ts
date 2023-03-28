import axios from 'axios';

const client = axios.create();

// local
client.defaults.baseURL = 'http://192.168.0.158:8080/';
// server
// client.defaults.baseURL = 'http://121.254.171.155:3003/';
client.defaults.withCredentials = true;

export default client;
