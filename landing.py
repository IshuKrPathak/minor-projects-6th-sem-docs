
import streamlit as st

def main():
    
    st.title("BimariPechano✨")
    

    st.header("Welcome to BimariDekho!")
    st.write("This is the main hero page of this website.")
    image_column, text_column = st.columns((9, 9))
    with image_column:
        st.image('https://th.bing.com/th/id/OIP.hc-Ls3YiIZtPW7nZHzbVkQHaFj?pid=ImgDet&w=800&h=600&rs=1')
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )

    def on_button_click():
     st.write('Button clicked!')
    if st.button('start here'):
      on_button_click()

if __name__ == "__main__":
    main()

