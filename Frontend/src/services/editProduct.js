import axios from 'axios';

const url = 'https://653b817d2e42fd0d54d539cb.mockapi.io/api/v1/product';

// fungsi mengubah data produk
export default async function editProduct(id, data) {
  try {
    const response = await axios.put(`${url}/${id}`, data);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}