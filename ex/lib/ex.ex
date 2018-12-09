defmodule Ex do
  def classify(params_to_classify) do
    receiver = {:py_process, :"py@127.0.0.1"}

    encoded_params_to_classify =
      Jason.encode!([
        params_to_classify.sepal_length,
        params_to_classify.sepal_width,
        params_to_classify.petal_length,
        params_to_classify.petal_width
      ])

    receiver
    |> GenServer.call({:classify, encoded_params_to_classify})
    |> Jason.decode!()
  end
end
