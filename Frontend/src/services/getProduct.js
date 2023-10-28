import axios from 'axios';

const url = 'https://653b817d2e42fd0d54d539cb.mockapi.io/api/v1/product';

// fungsi untuk mengambil data produk
export default async function getProduct() {
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}