import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const initialState:any={};

const responseSlice = createSlice({
  name: "response",
  initialState,
  reducers: {
    
    setFullResponse: (state, action: PayloadAction<any>) => {
      state = action.payload;
    },
  },
});

export const { setFullResponse } = responseSlice.actions;
export default responseSlice.reducer;
