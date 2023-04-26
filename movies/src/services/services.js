import axiosInstance from './config'

export const getStore = async () => {
    return axiosInstance({
      url: `store/store/`,
      method: 'get'
    })
      .then((response) => response.data)
      .catch(() => [])
  }

  export const getFilms = async () => {
    return axiosInstance({
      url: `films/films/`,
      method: 'get'
    })
      .then((response) => response.data)
      .catch(() => [])
  }

  export const getInventory = async () => {
    return axiosInstance({
      url: `store/inventory/`,
      method: 'get'
    })
      .then((response) => response.data)
      .catch(() => [])
  }

  export const createInventory = async (data) => {
    return axiosInstance({
      url: `store/create-inventory/`,
      method: 'post',
      data: data
    })
      .then((response) => response.data)
      .catch(() => [])
  }

  export const deleteInventory = async (id) => {
    return axiosInstance({
      url: `store/delete-inventory/${id}/`,
      method: 'delete'
    })
      .then((response) => response.data)
      .catch(() => [])
  }

  export const getClients = async () => {
    return axiosInstance({
      url: `store/customer/`,
      method: 'get'
    })
      .then((response) => response.data)
      .catch(() => [])
  }

  export const updateInventory = async (data, id) => {
    return axiosInstance({
      url: `store/update-inventory/${id}/`,
      method: 'put',
      data: data
    })
      .then((response) => response.data)
      .catch(() => [])
  }

  
  
