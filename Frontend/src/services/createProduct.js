import axios from 'axios';
const url = 'https://6524d54eea560a22a4ea26a4.mockapi.io/api/v1/product';

// fungsi membuat atau menambah produk baru
export default async function createProduct(product) {
  try {
    const response = await axios.post(url, product);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}